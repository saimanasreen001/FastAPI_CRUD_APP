from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from .auth import (
    get_current_user, create_access_token, get_password_hash, verify_password, ACCESS_TOKEN_EXPIRE_MINUTES
)

app = FastAPI()

students = {}


class Student(BaseModel):
    name: str
    gender: str
    age: int


# Dummy user for demonstration
fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": get_password_hash("admin123")
    }
}


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(
        data={"sub": user["username"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student, username: str = Depends(get_current_user)):
    if student_id in students:
        raise HTTPException(status_code=404, detail="Student already exists")
    students[student_id] = student
    return {"message": "student added successfully", "student": student}


@app.get("/students/{student_id}")
def read_student(student_id: int, username: str = Depends(get_current_user)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student, username: str = Depends(get_current_user)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id] = student
    return {"message": "student updated succesfully", "student": student}


@app.delete("/students/{student_id}")
def delete_student(student_id: int, username: str = Depends(get_current_user)):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="student not found")
    del students[student_id]
    return {"message": "student deleted successfully"}


@app.get("/")
def root():
    return {
        "endpoints": {
            "create": "POST/students/{student_id}",
            "read": "GET/students/{student_id}",
            "update": "PUT/students/{student_id}",
            "delete": "DELETE/students/{student_id}"
        }
    }