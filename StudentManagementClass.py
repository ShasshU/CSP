# Student Management System using Classes
# Made by: Shassh Umamaheswaran

# Student class to store individual student data
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    # Function to display this student's details
    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}")


# StudentManager class to manage a list of Student objects
class StudentManager:
    def __init__(self):
        self.students = []

    # Add a new student
    def add_student(self, name, student_id, grade):
        # Check if student ID already exists
        for student in self.students:
            if student.student_id == student_id:
                print("Error: Student ID already exists")
                return
        self.students.append(Student(name, student_id, grade))
        print("Student added successfully!")

    # Display all students
    def display_all_students(self):
        if len(self.students) == 0:
            print("\nNo students in the system")
        else:
            for student in self.students:
                student.display()

    # Find and return student by ID
    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.display()
                return student
        print("Student not found")
        return None

    # Remove student by ID
    def remove_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student removed successfully!")
                return
        print("Student not found")

    # Update grade of a student
    def update_student_grade(self, student_id, new_grade):
        student = self.find_student_by_id(student_id)
        if student is not None:
            student.grade = new_grade
            print("Grade updated successfully!")


# Display the main menu
def start_display():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Find Student by ID")
    print("4. Remove Student by ID")
    print("5. Update Student Grade")
    print("6. Exit")


# Main program loop
def main():
    manager = StudentManager()

    while True:
        start_display()
        choice = input("\nChoose an option: ")

        try:
            if choice == '1':
                name = input("Enter student name: ")
                student_id = int(input("Enter student ID: "))
                grade = float(input("Enter student grade: "))
                manager.add_student(name, student_id, grade)

            elif choice == '2':
                manager.display_all_students()

            elif choice == '3':
                student_id = int(input("Enter student ID to find: "))
                manager.find_student_by_id(student_id)

            elif choice == '4':
                student_id = int(input("Enter student ID to remove: "))
                manager.remove_student_by_id(student_id)

            elif choice == '5':
                student_id = int(input("Enter student ID to update grade: "))
                new_grade = float(input("Enter new grade: "))
                manager.update_student_grade(student_id, new_grade)

            elif choice == '6':
                print("\nExiting program...")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 6")

        except ValueError:
            print("Invalid input! Please enter numeric values for ID and grade")


# Run the program
if __name__ == "__main__":
    main()
