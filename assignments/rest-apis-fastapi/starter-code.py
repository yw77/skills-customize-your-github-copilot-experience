from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# TODO: Define the Book model with fields: id, title, author, year
# Use Pydantic's Field() to add validation constraints


# In-memory list of books
books = []


@app.get("/")
def root():
    # TODO: Return a welcome message
    pass


@app.get("/books")
def get_books():
    # TODO: Return the list of all books
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return a single book by ID, or raise a 404 error
    pass


@app.post("/books", status_code=201)
def create_book(book: dict):
    # TODO: Add a new book to the list and return it
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict):
    # TODO: Update an existing book's details, or raise a 404 error
    pass


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Remove a book from the list, or raise a 404 error
    pass
