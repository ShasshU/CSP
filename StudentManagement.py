
student_names = []
student_ids = []
student_grades = []


def start_display():
    print("Student Management System")
    print("")
    print("Choose one of the following:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Find Student by ID")
    print("4. Remove Student by ID")
    print("5. Update Student Grade")
    print("6. Exit")


def add_student(name, student_id, grade):

    # Check if student ID already exists
    if student_id in student_ids:
        print(f"Error: Student ID {student_id} already exists!")
        return
    
    # Add student data to respective lists
    student_names.append(name)
    student_ids.append(student_id)
    student_grades.append(grade)
    
    print(f"Student added successfully!")


def display_all_students():

    if len(student_ids) == 0:
        print("\nNo students in the system.")
        return
    
    print("\n" + "-"*50)
    for i in range(len(student_ids)):
        print(f"ID: {student_ids[i]}, Name: {student_names[i]}, Grade: {student_grades[i]}")
    print("-"*50)


def find_student_by_id(student_id):
    
    if student_id in student_ids:
        index = student_ids.index(student_id)
        print(f"\nID: {student_ids[index]}, Name: {student_names[index]}, Grade: {student_grades[index]}")
    else:
        print(f"\nStudent not found.")


def remove_student_by_id(student_id):
    
    if student_id in student_ids:
        index = student_ids.index(student_id)
        
        # Remove from all lists
        student_names.pop(index)
        student_ids.pop(index)
        student_grades.pop(index)
        
        print(f"\nStudent removed successfully!")
    else:
        print(f"\nStudent not found.")


def update_student_grade(student_id, new_grade):
   
    if student_id in student_ids:
        index = student_ids.index(student_id)
        student_grades[index] = new_grade
        print(f"\nGrade updated successfully!")
    else:
        print(f"\nStudent not found.")


def main():
    
    while True:
        start_display()
        
        # Get user's menu choice
        choice = input("\nChoose an option: ").strip()
        
        if choice == '1':
            # Add Student
            name = input("Enter student name: ")
            student_id = int(input("Enter student ID: "))
            grade = float(input("Enter student grade: "))
            
            add_student(name, student_id, grade)
        
        elif choice == '2':
            # Display All Students
            display_all_students()
        
        elif choice == '3':
            # Find Student by ID
            student_id = int(input("Enter student ID to find: "))
            find_student_by_id(student_id)
        
        elif choice == '4':
            # Remove Student by ID
            student_id = int(input("Enter student ID to remove: "))
            remove_student_by_id(student_id)
        
        elif choice == '5':
            # Update Student Grade
            student_id = int(input("Enter student ID to update grade: "))
            new_grade = float(input("Enter new grade: "))
            update_student_grade(student_id, new_grade)
        
        elif choice == '6':
            # Exit program
            print("\nExiting program...")
            break
        
        else:
            # Handle invalid menu choice
            print("\nInvalid choice! Please enter a number between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()