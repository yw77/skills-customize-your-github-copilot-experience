# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build RESTful APIs using Python's FastAPI framework. You will create a simple API that handles CRUD (Create, Read, Update, Delete) operations for managing a collection of books.

## 📝 Tasks

### 🛠️	Set Up a Basic FastAPI Server

#### Description
Install FastAPI and Uvicorn, then create a basic API server that runs on `http://localhost:8000`. Define a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install `fastapi` and `uvicorn` packages
- Create a FastAPI app instance in `main.py`
- Define a `GET /` endpoint that returns `{"message": "Welcome to the Book API"}`
- Run successfully with `uvicorn main:app --reload`

### 🛠️	Create CRUD Endpoints for Books

#### Description
Define a `Book` model using Pydantic with fields for `id`, `title`, `author`, and `year`. Then implement API endpoints to create, read, update, and delete books from an in-memory list.

#### Requirements
Completed program should:

- Define a `Book` Pydantic model with fields: `id` (int), `title` (str), `author` (str), `year` (int)
- Implement `GET /books` to return the full list of books
- Implement `GET /books/{book_id}` to return a single book by its ID, or a 404 error if not found
- Implement `POST /books` to add a new book and return it with a 201 status code
- Implement `PUT /books/{book_id}` to update an existing book's details
- Implement `DELETE /books/{book_id}` to remove a book from the list

### 🛠️	Add Input Validation and Error Handling

#### Description
Enhance your API by adding proper input validation using Pydantic and returning meaningful error responses when something goes wrong.

#### Requirements
Completed program should:

- Validate that `year` is between 1000 and the current year
- Validate that `title` and `author` are non-empty strings
- Return a `404` response with a descriptive message when a book is not found
- Return a `422` response when invalid data is submitted
