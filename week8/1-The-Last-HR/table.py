from get_info import GetInfo
import sqlite3

hack_info = GetInfo("https://hackbulgaria.com/api/students/")
db = sqlite3.connect("students.db")
cursor = db.cursor()

table_students = """CREATE TABLE IF NOT EXISTS
Students(id INTEGER PRIMARY KEY, name TEXT, github TEXT )"""
db.execute(table_students)

table_courses = """CREATE TABLE IF NOT EXISTS
Courses(id INTEGER PRIMARY KEY, course TEXT )"""
db.execute(table_courses)

table_student_to_course = """CREATE TABLE IF NOT EXISTS
Student_to_Course(id_s INTEGER, id_c INTEGER,
FOREIGN KEY (id_s) REFERENCES Students(id),
FOREIGN KEY (id_c) REFERENCES Courses(id))
"""
db.execute(table_student_to_course)
db.commit()

# Insert students
db.executemany("INSERT INTO Students(name, github) VALUES(?,?)", hack_info.get_name_and_github())
db.commit()

# Insert courses
db.executemany("INSERT INTO Courses(course) VALUES(?)", hack_info.get_courses())
db.commit()

# Show courses
db.execute("SELECT course FROM Courses")

# Get students id and names
students_id_name = db.execute("SELECT id, name FROM Students")
students_dict ={students_id_name[1]: students_id_name[0] for studen in students_id_name}

db.commit()
