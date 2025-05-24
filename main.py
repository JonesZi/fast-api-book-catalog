from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from typing import List

from models import Book
from database import engine, create_db_and_tables

app = FastAPI()

create_db_and_tables()

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book

@app.get("/books/", response_model=List[Book])
def read_books():
    with Session(engine) as session:
        books = session.exec(select(Book)).all()
        return books

@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

# // Old requests from before adding SQLite database
# @app.post("/books")
# def create_book(book: Book):
#     books.append(book)
#     return book

# @app.put("/books/{book_id}")
# def update_book(book_id: int, updated_book: Book):
#     for i, book in enumerate(books):
#         if book.id == book_id:
#             books[i] = updated_book
#             return updated_book
#     raise HTTPException(status_code=404, detail="Book not found")

# @app.delete("/books/{book_id}")
# def delete_book(book_id: int):
#     for i, book in enumerate(books):
#         if book.id == book_id:
#             del books[i]
#             return {"message": "Book deleted"}
#     raise HTTPException(status_code=404, detail="Book not found")