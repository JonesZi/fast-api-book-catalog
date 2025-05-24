from fastapi import FastAPI, HTTPException
from models import Book
from books_data import books

app = FastAPI()

# FastAPI Anwendung für einen Buchkatalog
@app.get("/")
def read_root():
    return {"message": "Willkomen im Buchkatalog!"}

@app.get("/books")
def get_books():
    return books 

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Buch nicht gefunden")

@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")