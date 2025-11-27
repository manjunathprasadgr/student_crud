from repository.student_repository import StudentRepository
from models.student import Student

class StudentService:
    def __init__(self):
        self.repo = StudentRepository()

    def create_student(self, name, age):
        student = Student(name, age)
        self.repo.add_student(student)
        return "Student created!"

    def get_students(self):
        return self.repo.get_all()

    def update_student(self, student_id, name, age):
        self.repo.update(student_id, name, age)
        return "Student updated!"

    def delete_student(self, student_id):
        self.repo.delete(student_id)
        return "Student deleted!"