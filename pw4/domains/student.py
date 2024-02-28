class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}  # Store marks for each course, with credit as key

    def input_info(self):
        # Implement input logic here
        pass

    def list_info(self):
        print(f"Student ID: {self.id}, Name: {self.name}, DoB: {self.dob}")

    def input_marks(self, course_id, credit):
        # Implement mark input logic here
        pass

    def calculate_gpa(self):
        # Implement GPA calculation logic here
        pass
