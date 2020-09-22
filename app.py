from flask import Flask, render_template, request, redirect, url_for

import json
import os
import random

# To create the Flask app
app = Flask(__name__)

database = []
with open('data.json', 'r') as fp:
    database = json.load(fp)


@app.route('/')
def home():
    return "Home page"


@app.route('/books')
def show_books():
    return render_template('books.template.html', database=database)


@app.route('/books/create')
def create_book():
    return render_template('create_book.template.html')


@app.route('/books/create', methods=['POST'])
def process_create_book():
    new_book = {
        "id": random.randint(10000, 99999),
        "title": request.form.get("title"),
        "author": request.form.get("author")
    }
    database.append(new_book)

    with open('data.json', 'w') as fp:
        json.dump(database, fp)

    return redirect(url_for('show_books'))


if __name__ == '__main__':
    # this is the line that starts the server
    app.run(host='0.0.0.0',
            port=8080,
            debug=True)
