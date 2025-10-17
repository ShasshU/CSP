# Student Management System
# Made by: Shassh Umamaheswaran

# Lists to store student information
student_names = []
student_ids = []
student_grades = []

# Function to display the main menu
def start_display():
    print("\nStudent Management System")
    print("--------------------------")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Find Student by ID")
    print("4. Remove Student by ID")
    print("5. Update Student Grade")
    print("6. Exit")

# Function to add a student
def add_student(name, student_id, grade):
    # Check if student ID already exists
    if student_id in student_ids:
        print(f"Error: Student ID {student_id} already exists.")
        return
    
    # Add student data to lists
    student_names.append(name)
    student_ids.append(student_id)
    student_grades.append(grade)
    
    print("Student added successfully!")

# Function to display all students
def display_all_students():
    if len(student_ids) == 0:
        print("\nNo students in the system.")
        return
    
    # Loop through all students and display information
    for i in range(len(student_ids)):
        print(f"ID: {student_ids[i]}, Name: {student_names[i]}, Grade: {student_grades[i]}")

# Function to find a student by ID
def find_student_by_id(student_id):
    if student_id in student_ids:
        index = student_ids.index(student_id)
        print(f"\nID: {student_ids[index]}, Name: {student_names[index]}, Grade: {student_grades[index]}")
    else:
        print("\nStudent not found.")

# Function to remove a student by ID
def remove_student_by_id(student_id):
    if student_id in student_ids:
        index = student_ids.index(student_id)
        
        # Remove student from all lists
        student_names.pop(index)
        student_ids.pop(index)
        student_grades.pop(index)
        
        print("\nStudent removed successfully!")
    else:
        print("\nStudent not found.")

# Function to update a student's grade
def update_student_grade(student_id, new_grade):
    if student_id in student_ids:
        index = student_ids.index(student_id)
        student_grades[index] = new_grade
        print("\nGrade updated successfully!")
    else:
        print("\nStudent not found.")

# Main function to run the program
def main():
    while True:
        start_display()  # Show menu
        
        # Get user choice
        choice = input("\nChoose an option: ")

        try:
            # Add Student
            if choice == '1':
                name = input("Enter student name: ")
                student_id = int(input("Enter student ID: "))
                grade = float(input("Enter student grade: "))
                add_student(name, student_id, grade)
            
            # Display All Students
            elif choice == '2':
                display_all_students()
            
            # Find Student by ID
            elif choice == '3':
                student_id = int(input("Enter student ID to find: "))
                find_student_by_id(student_id)
            
            # Remove Student by ID
            elif choice == '4':
                student_id = int(input("Enter student ID to remove: "))
                remove_student_by_id(student_id)
            
            # Update Student Grade
            elif choice == '5':
                student_id = int(input("Enter student ID to update grade: "))
                new_grade = float(input("Enter new grade: "))
                update_student_grade(student_id, new_grade)
            
            # Exit program
            elif choice == '6':
                print("\nExiting program...")
                break
            
            # Handle invalid menu choice
            else:
                print("\nInvalid choice! Please enter a number between 1 and 6.")

        except ValueError:
            # Handle invalid input for ID or grade
            print("\nInvalid input! Please enter numeric values for ID and grade.")

# Run the program
if __name__ == "__main__":
    main()
