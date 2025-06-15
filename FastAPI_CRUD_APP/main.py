from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

students={}

class Student(BaseModel):
    name:str
    gender:str
    age:int

@app.post("/students/{student_id}")
def create_student(student_id:int, student:Student):
    if student_id in students:
        raise HTTPException(status_code=404,detail="Student already exists")
    students[student_id]=student
    return {"message":"student added successfully","student":student}

@app.get("/students/{student_id}")
def read_student(student_id:int):
    if student_id not in students:
        raise HTTPException(status_code=404,detail="Student not found")
    return students[student_id]

@app.put("/students/{student_id}")
def update_student(student_id:int,student:Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail= "Student not found")
    students[student_id]=student
    return {"message":"student updated succesfully","student":student}

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        raise HTTPException(status_code=404,detail="student not found")
    del students[student_id]
    return {"message":"student deleted successfully"}

@app.get("/")
def root():
    return {
        "endpoints":{
            "create":"POST/students/{student_id}",
            "read":"GET/students/{student_id}",
            "update":"PUT/students/{student_id}",
            "delete":"DELETE/students/{student_id}"
        }
    }