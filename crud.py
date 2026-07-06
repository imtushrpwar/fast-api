from fastapi import FastAPI, status
from typing import Optional
from pydantic import BaseModel

from fastapi.exceptions import HTTPException

# In-memory list of books used as a simple data store.
books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }
]

app = FastAPI()

@app.get("/books/")
async def get_books():
    # Return the full list of books.
    return {"books": books}

@app.get("/book/{id}")
async def get_book(id: int):
    # Retrieve a single book by its ID. Return 404 if not found.
    for book in books:
        if book["id"] == id:
            return {"book": book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

class Book(BaseModel):
    # Schema for creating a new book.
    title: str
    author: str
    year: int

@app.post("/books/")
async def create_book(book: Book):
    # Add a new book to the list.
    newbook = book.model_dump()
    books.append(newbook)
    return {"Message": f"Book '{book.title}' added successfully!", "Book": book}


class BookUpdate(BaseModel):
    # Schema for updating a book with optional fields.
    title: Optional[str] = None 
    author: Optional[str] = None
    year: Optional[int] = None

@app.put("/book/{id}")
async def update_book(id: int, book_update: BookUpdate):
    # Update the specified book with provided values.
    for book in books:
        if book["id"] == id:
            if book_update.title is not None:
                book["title"] = book_update.title
            if book_update.author is not None:
                book["author"] = book_update.author
            if book_update.year is not None:
                book["year"] = book_update.year
            return {"Message": f"Book with ID {id} updated successfully!", "Book": book}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")



@app.delete("/book/{id}")
async def delete_book(id: int):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return {"Message": f"Book with ID {id} deleted successfully!"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")