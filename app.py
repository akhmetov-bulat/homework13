import json

from flask import Flask, render_template, request

app = Flask(__name__)


def read_books_json():
    with open('books.json', encoding='utf-8') as f:
        file = f.read()
        if file:
            books = json.load(f)
            return books
        return {}


@app.route('/books/<int:book_id>')
def get_book_by_id(book_id: int):
    books = read_books_json()
    if books:
        for book in books:
            if book[id] == book_id:
                return book
        return "there is no book on this id"
    return "bookshelf is clear"






if __name__ == '__main__':
    app.run(debug=True)