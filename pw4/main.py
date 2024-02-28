import curses
from domains import student
from input import get_integer, get_string
from output import print_courses, print_students

def main(stdscr):
    # Input student information
    num_students = get_integer(stdscr, "Enter the number of students: ")
    students = []
    for _ in range(num_students):
        student_obj = student.Student(None, None, None)
        student_obj.input_info()  # Implement input logic here (possibly using input.py)
        students.append(student_obj)

    # Input course information
    num_courses = get_integer(stdscr, "Enter the number of courses: ")
    courses = []
    for _ in range(num_courses):
        course_obj = student.Course(None, None)
        course_obj.input_info()  # Implement input logic here (possibly using input.py)
        courses.append(course_obj)

    # Input marks for each course
    for course in courses:
        for student in students:
            credit = get_integer(stdscr, f"Enter credits for {course.name}: ")
            student.input_marks(course.id, credit)  # Implement mark input logic here (possibly using input.py)

    stdscr.clear()  # Clear screen for output

    # Calculate and sort students by GPA
    for student in students:
        student.gpa = student.calculate_gpa()  # Implement GPA calculation logic (possibly in student.py)
    students.sort(key=lambda s: s.gpa, reverse=True)  # Sort by GPA descending

    # Print courses, students, marks, and GPA
    print_courses(stdscr, courses)
    print_students(stdscr, students)

if __name__ == "__main__":
    curses.wrapper(main)
