managementList = []

print("Student Management System")
print("Choose one of the following: ")
print("1. Add Student")
print("2. Display all students")
print("3. Find student by ID")
print("4. Remove student by ID")
print("5. Update student grade")
print("6. Exit")

userChoice = input("Choose an option: ")

if userChoice == "1":
    name = input("Enter student name: ")
    ID = input("Enter student ID: ")
    grade = input("Enter students grade: ")

    managementList.append(ID)
    managementList.append(name)
    managementList.append(grade)

elif userChoice == "2":
    print(managementList)

elif userChoice == "3":
    findStudent = input("Find student by ID")
    if findStudent in managementList:
        index = managementList.index(findStudent)
        print("ID: " + managementList[index])
        print("Name: " + managementList[index + 1])
        print("Grade: " + managementList[index + 2])
    else:
        print("Student not found")

elif userChoice == "4":
    removeStudent = input("Enter an ID to comment")
    if removeStudent in managementList:
        index = managementList.index(removeStudent)
        managementList.pop(index)
        managementList.pop(index)
        managementList.pop(index)
        print("Student removed")
    else:
        print("Student not found")

elif userChoice == "5":
    updateStudent = input("Enter student ID to update grade")
    if updateStudent in managementList:
        index = managementList.index(updateStudent)
        newGrade = input("Enter students new grade")
        managementList[index + 2] = newGrade
        print("Grade updated")
    else:
        print("Student not found")

elif userChoice == "6":
    print("Exiting program")
    exit()

else:
    print("Invalid choice, please try again and enter a number between 1-6")
        






