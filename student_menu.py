import os

# File to store student records
FILE_NAME = "students.txt"

# Function to add a new student record
def add_student():
    name = input("Enter student name: ")
    student_class = input("Enter student class: ")
    roll_no = input("Enter student roll number: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"Name: {name}, Class: {student_class}, Roll No: {roll_no}\n")
    print("Student record added successfully!\n")

# Function to view all student records
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()
        if not records:
            print("No records found.\n")
            return

        print("Student Records:")
        for i, record in enumerate(records, start=1):
            print(f"{i}. {record.strip()}")
        print()

# Function to remove a specific student record
def remove_student():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    view_students()
    try:
        record_no = int(input("Enter the record number to remove: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()

    if record_no < 1 or record_no > len(records):
        print("Invalid record number.\n")
        return

    del records[record_no - 1]

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    print("Record removed successfully!\n")

# Function to clear all student records
def clear_records():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("All records cleared successfully!\n")
    else:
        print("No records to clear.\n")

# Main menu-driven program
def menu():
    while True:
        print("Menu:")
        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Remove a Record")
        print("4. Clear All Records")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            clear_records()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()