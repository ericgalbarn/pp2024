# List to store student information
students = []  
# List to store course information
courses = []  

# Input functions
def input_student_info():
    """Inputs student information: id, name, DoB."""
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (YYYY-MM-DD): ")
    students.append((id, name, dob))  # Add student tuple to the list

def input_course_info():
    """Inputs course information: id, name."""
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append((id, name))  # Add course tuple to the list

def input_marks_for_course(course_id):
    """Inputs marks for all students in a given course."""
    for student in students:
        marks = int(input(f"Enter marks for {student[1]} in course {course_id}: "))
        # Store marks in a dictionary, keyed by student ID
        if student[0] not in marks_dict:
            marks_dict[student[0]] = {}
        marks_dict[student[0]][course_id] = marks

# Listing functions
def list_courses():
    """Prints a list of all courses."""
    for course in courses:
        print(f"Course ID: {course[0]}, Course Name: {course[1]}")

def list_students():
    """Prints a list of all students."""
    for student in students:
        print(f"Student ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_marks_for_course(course_id):
    """Prints marks for all students in a given course."""
    print(f"Marks for Course {course_id}:")
    for student_id, marks in marks_dict.items():
        print(f"{student_id}: {marks.get(course_id, 'N/A')}")  # Handle missing marks

# Main program
marks_dict = {}  # Dictionary to store student marks for each course

# Input student information
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    input_student_info()

# Input course information
num_courses = int(input("Enter the number of courses: "))
for _ in range(num_courses):
    input_course_info()

# Input marks for each course
for course_id, course_name in courses:
    input_marks_for_course(course_id)

# List courses, students, and marks
list_courses()
list_students()
show_marks_for_course(int(input("Enter course ID to view marks: ")))
