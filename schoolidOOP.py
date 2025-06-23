class Student:
    def __init__(self, name, age, student_id, grade):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grade = grade
    def update_details(self, name=None, age=None, grade=None):
        if name:
            self.name = name
        if age:
            self.age = age
        if grade:
            self.grade = grade
        print(f"Updated details of student ID: {self.student_id}")
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
class School:
    def __init__(self):
        self.students = {}
    def add_student(self, name, age, student_id, grade):
        if student_id not in self.students:
            student = Student(name, age, student_id, grade)
            self.students[student_id] = student
            print(f"Added student: {name}")
        else:
            print(f"Student with ID {student_id} already exists.")
    def remove_student(self, student_id):
        if student_id in self.students:
            removed_student = self.students.pop(student_id)
            print(f"Removed student: {removed_student.name}")
        else:
            print(f"Student with ID {student_id} not found.")
    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id in self.students:
            student = self.students[student_id]
            student.update_details(name, age, grade)
        else:
            print(f"Student with ID {student_id} not found.")
    def display_students(self):
        if not self.students:
            print("No students to display.")
        else:
            for student in self.students.values():
                print(student)
school = School()
school.add_student("Alice", 14, 1, "9th")
school.display_students()
school.update_student(1, age=15, grade="10th")
school.display_students()