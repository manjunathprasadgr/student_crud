from fastapi import FastAPI
from service.student_service import StudentService

app = FastAPI()
service = StudentService()

@app.post("/students")
def create_student(name: str, age: int):
    return service.create_student(name, age)

@app.get("/students")
def get_students():
    return service.get_students()

@app.put("/students/{student_id}")
def update_student(student_id: int, name: str, age: int):
    return service.update_student(student_id, name, age)

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    return service.delete_student(student_id)
