import sqlite3

class Database:
    def __init__(self):
        self.db_name = "student.db"
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        con = self.connect()
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
            )
        """)
        con.commit()
        con.close()