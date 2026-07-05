from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# Simple FastAPI application demonstrating three endpoints:
# - GET / returns a hello message
# - GET /greet returns a greeting
# - GET /items/{name} returns item info and optional age query param
app = FastAPI()


@app.get("/")
async def read_root():
    # Root endpoint
    return {"Message": "Hello World"}


@app.get("/greet")
async def greet():
    # Greeting endpoint
    return {"Message": "Hello from FastAPI!"}


@app.get("/items/{name}")
async def read_item(name: str, age: Optional[int] = None):
    # Item endpoint with optional age parameter
    if age is None:
        return {"Message": f"Item : {name}, Age: Not specified"}
    return {"Message": f"Item : {name}, Age: {age}"}

class Student(BaseModel):
    name: str
    age: int
    grade: Optional[str] = None

@app.post("/create_student/")
async def create_student(student: Student):
    # Endpoint to create a student
    return {"Message": f"Student {student.name} created successfully!", "Student": student}     

