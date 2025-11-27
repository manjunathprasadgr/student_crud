from db.database import Database

class StudentRepository:
    def __init__(self):
        self.db = Database()

    def add_student(self, student):
        con = self.db.connect()
        cur = con.cursor()
        cur.execute("INSERT INTO students (name, age) VALUES (?, ?)",
                    (student.name, student.age))
        con.commit()
        con.close()

    def get_all(self):
        con = self.db.connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM students")
        data = cur.fetchall()
        con.close()
        return data

    def update(self, student_id, name, age):
        con = self.db.connect()
        cur = con.cursor()
        cur.execute("UPDATE students SET name=?, age=? WHERE id=?",
                    (name, age, student_id))
        con.commit()
        con.close()

    def delete(self, student_id):
        con = self.db.connect()
        cur = con.cursor()
        cur.execute("DELETE FROM students WHERE id=?", (student_id,))
        con.commit()
        con.close()
