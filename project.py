from fastapi import FastAPI, Depends
from database import get_db, engine, Base
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app = FastAPI()

class BookStore(BaseModel):
    id: int
    title: str
    author: str
    year: int

@app.post("/books/")
def create_book(book: BookStore, db: Session = Depends(get_db)):
    new_book = model.Book(title=book.title, author=book.author, year=book.year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books/")
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(model.Book).offset(skip).limit(limit).all()
    return books