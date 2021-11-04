import json
from flask import Flask, request, Response

app = Flask(__name__)


def read_books_json():
    with open('books.json',"r", encoding='utf-8') as f:
        file = f.read()
        if file:
            books = json.loads(file)
            return books
        return []

def write_json(books):
    pass


@app.route('/books/<int:book_id>')
def get_book_by_id(book_id: int):
    books = read_books_json()
    if books:
        for book in books:
            if book['id'] == book_id:
                return Response(json.dumps(book, ensure_ascii = False), content_type='application/json', status=400)
        return Response("there is no book on this id", content_type="text/html", status=404)
    return Response("bookshelf is clear", content_type='text/html', status=404)


@app.route('/books/add', methods = ['POST'])
def add_book():
    books = read_books_json()
    def new_id():
        max_id = 0
        for book in books:
            if book['id'] > max_id:
                max_id = book['id']
            return max_id + 1
    book = request.get_json()
    book['id'] = new_id()
    book['ISBN'] = new_isbn()
    books.append(book)
    with open('books.json', 'w', encoding='utf-8',) as f:
        json.dump(books, f, ensure_ascii=False,indent='\t')
    return Response(json.dumps(books, ensure_ascii=False), content_type='application/json', status=201)




if __name__ == '__main__':
    app.run(debug=True)
