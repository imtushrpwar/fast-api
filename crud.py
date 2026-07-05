from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

books = [
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }
]

app = FastAPI()

@app.get("/books/")
async def get_books():
    return {"books": books}

class Book(BaseModel):
    title: str
    author: str
    year: int

@app.post("/books/")
async def create_book(book: Book):
    newbook = book.model_dump()
    books.append(newbook)
    return {"Message": f"Book '{book.title}' added successfully!", "Book": book}