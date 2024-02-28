import math
import numpy as np
from curses import wrapper

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}  # Store marks for each course, with credit as key

    def input_info(self, stdscr):
        """Inputs student information using curses."""
        stdscr.addstr("Enter student ID: ")
        stdscr.refresh()
        self.id = stdscr.getstr().decode()

        stdscr.addstr("Enter student name: ")
        stdscr.refresh()
        self.name = stdscr.getstr().decode()

        stdscr.addstr("Enter student date of birth (YYYY-MM-DD): ")
        stdscr.refresh()
        self.dob = stdscr.getstr().decode()

    def list_info(self):
        """Prints student information."""
        print(f"Student ID: {self.id}, Name: {self.name}, DoB: {self.dob}")

    def input_marks(self, stdscr, course_id, credit):
        """Inputs marks for a student in a given course using curses."""
        stdscr.addstr(f"Enter marks for {self.name} in course {course_id} (credits: {credit}): ")
        stdscr.refresh()
        mark = math.floor(float(stdscr.getstr().decode()))  # Round down to 1 decimal
        self.marks[course_id] = (mark, credit)  # Store mark and credit as a tuple

    def calculate_gpa(self):
        """Calculates average GPA for the student."""
        total_weighted_marks = 0
        total_credits = 0
        for mark, credit in self.marks.values():
            total_weighted_marks += mark * credit
            total_credits += credit
        return total_weighted_marks / total_credits if total_credits else 0


class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def input_info(self, stdscr):
        """Inputs course information using curses."""
        stdscr.addstr("Enter course ID: ")
        stdscr.refresh()
        self.id = stdscr.getstr().decode()

        stdscr.addstr("Enter course name: ")
        stdscr.refresh()
        self.name = stdscr.getstr().decode()

    def list_info(self):
        """Prints course information."""
        print(f"Course ID: {self.id}, Course Name: {self.name}")


def main(stdscr):
    """Main program using curses UI."""
    # Input student information
    num_students = int(stdscr.getstr("Enter the number of students: ").decode())
    students = []
    for _ in range(num_students):
        student = Student(None, None, None)
        student.input_info(stdscr)
        students.append(student)

    # Input course information
    num_courses = int(stdscr.getstr("Enter the number of courses: ").decode())
    courses = []
    for _ in range(num_courses):
        course = Course(None, None)
        course.input_info(stdscr)
        courses.append(course)

    # Input marks for each course
    for course in courses:
        for student in students:
            credit = int(stdscr.getstr(f"Enter credits for {course.name}: ").decode())
            student.input_marks(stdscr, course.id, credit)

    stdscr.clear()  # Clear screen for output

    # Calculate and sort students by GPA
    for student in students:
        student.gpa = student.calculate_gpa()
    students.sort(key=lambda s: s.gpa, reverse=True)  # Sort by GPA descending

    # Print courses, students, marks, and GPA
    stdscr.addstr("Courses:\n")
    stdscr.refresh()
    for course in courses:
        course.list_info()
        stdscr.addstr("\n")

    stdscr.addstr("Students:\n")
    stdscr.refresh()
    