import curses

def print_courses(stdscr, courses):
    stdscr.addstr("Courses:\n")
    stdscr.refresh()
    for course in courses:
        course.list_info()
        stdscr.addstr("\n")

def print_students(stdscr, students):
    stdscr.addstr("Students:\n")
    stdscr.refresh()
    for student in students:
        student.list_info()
        stdscr.addstr(f"\tGPA: {student.gpa:.2f}\n")  # Assuming gpa is calculated
