class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}  # Store marks for each course

    def input_info(self):
        """Inputs student information."""
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.dob = input("Enter student date of birth (YYYY-MM-DD): ")

    def list_info(self):
        """Prints student information."""
        print(f"Student ID: {self.id}, Name: {self.name}, DoB: {self.dob}")

    def input_marks(self, course_id):
        """Inputs marks for a student in a given course."""
        marks = int(input(f"Enter marks for {self.name} in course {course_id}: "))
        self.marks[course_id] = marks

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def input_info(self):
        """Inputs course information."""
        self.id = input("Enter course ID: ")
        self.name = input("Enter course name: ")

    def list_info(self):
        """Prints course information."""
        print(f"Course ID: {self.id}, Course Name: {self.name}")

students = []
courses = []

# Main program
if __name__ == "__main__":
    # Input student information
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        student = Student(None, None, None)  # Create empty student object
        student.input_info()
        students.append(student)

    # Input course information
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        course = Course(None, None)  # Create empty course object
        course.input_info()
        courses.append(course)

    # Input marks for each course
    for course in courses:
        for student in students:
            student.input_marks(course.id)

    # List courses, students, and marks
    for course in courses:
        course.list_info()
    for student in students:
        student.list_info()

    course_id = int(input("Enter course ID to view marks: "))
    for student in students:
        print(f"{student.id}: {student.marks.get(course_id, 'N/A')}")
