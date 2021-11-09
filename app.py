from flask import Flask, request, Response, jsonify
from utils import read_books_json, add_new_book


app = Flask(__name__)


@app.route('/books/<int:book_id>')
def get_book_by_id(book_id: int):
    books = read_books_json()
    if books:
        for book in books:
            if book['id'] == book_id:
                return jsonify(book),200
        return Response('Not Found',404)


@app.route('/books/add', methods=['post'])
def add_book():
    user_request = request.get_json()
    if {'name', 'author'} <= user_request.keys():
        books = add_new_book(user_request)
        return jsonify(books), 201
    return Response('Bad Request',400)


if __name__ == '__main__':
    app.run(debug=True)
