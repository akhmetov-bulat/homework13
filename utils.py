import json
from flask import Flask, request, Response, jsonify
from random import randint


def read_books_json():
    with open('books.json', "r", encoding='utf-8') as f:
        file = f.read()
        if file:
            books = json.loads(file)
            return books
        return []


def add_new_book(new_book):
    books = read_books_json()
    new_book['id'] = new_id(books)
    new_book['isbn'] = new_isbn(books)
    books.append(new_book)
    with open('books.json', 'w', encoding='utf-8', ) as f:
        json.dump(books, f, ensure_ascii=False, indent='\t')
    return books

def new_isbn(books):
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


def new_id(books):
    max_id = 0
    for book in books:
        if book['id'] > max_id:
            max_id = book['id']
    return max_id + 1
