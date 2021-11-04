import json
from flask import Flask, request, Response
from random import randint

app = Flask(__name__)


def read_books_json():
    with open('books.json', "r", encoding='utf-8') as f:
        file = f.read()
        if file:
            books = json.loads(file)
            return books
        return []


def new_isbn():
    books = read_books_json()
    unique_isbn = False
    while not unique_isbn:
        isbn_list = []
        isbn_list.append(str(randint(100, 999)))
        isbn_list.append(str(randint(0, 9)))
        isbn_list.append(str(randint(100, 999)))
        isbn_list.append('0' + str(randint(1000, 9999)))
        isbn_list.append(str(randint(0, 9)))
        isbn = "-".join(isbn_list)
        for book in books:
            if book['isbn'] == isbn:
                continue
        unique_isbn = True
        return isbn


@app.route('/books/<int:book_id>')
def get_book_by_id(book_id: int):
    books = read_books_json()
    if books:
        for book in books:
            if book['id'] == book_id:
                return Response(json.dumps(book, ensure_ascii=False), content_type='application/json', status=400)
        return Response("there is no book on this id", content_type="text/html", status=404)
    return Response("bookshelf is clear", content_type='text/html', status=404)


@app.route('/books/add', methods=['PUT'])
def add_book():
    books = read_books_json()
    def new_id():  # В роут создания книги добавьте генерацию id
        max_id = 0
        for book in books:
            if book['id'] > max_id:
                max_id = book['id']
        return max_id + 1
    new_book = request.get_json()
    new_book['id'] = new_id()
    new_book['isbn'] = new_isbn()
    books.append(new_book)
    with open('books.json', 'w', encoding='utf-8',) as f:
        json.dump(books, f, ensure_ascii=False, indent='\t')
    return Response(json.dumps(books, ensure_ascii=False), content_type='application/json', status=201)


if __name__ == '__main__':
    app.run(debug=True)
