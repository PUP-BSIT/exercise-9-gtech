import os

# Make the code readable as it is
# add comments per block or if necessary
# make sure to avoid magic values
# add tasks and assign it to a member if there is anything else needed

# This is a sample list of dictionaries
student_record = [{
                    "student_id": "123456789",
                    "full_name": "Adriel Joseph Dimayuga",
                    "program": "BSIT",
                    "contact_number": "12345678900",
                    "address": "Adriel Joseph address"
                   },
                  {
                    "student_id": "987654321",
                    "full_name": "AJ",
                    "program": "BSIT",
                    "contact_number": "12345678900",
                    "address": "AJ address"
                  }]

def clear_screen():
    os.system('cls')
    os.system('clear')
    
def add_student():
    # TODO (Grace Lim):
    # Add a function that allows the user to input the
    # following student details:
    # A data record should contain 5 fields
    # - Student ID (Max 9 numbers) (Primary Key)
    # - Full Name
    # - Program
    # - Contact Number (Max 11 numbers)
    # - Address
    # All records should be contained in a list
    # Add restrictions
    # Ask if the user wants to add another student record (y / n)
    # Add clear screen everytime the user adds another student record
    pass


def list_students():
    # TODO (Rain Romero):
    # Add a function to list/display all student records in the format:
    # Student ID :               123456789
    # Student Name :             Juan Tamad
    # Student Program :          BSIT
    # Contact Information:       12345678900
    # Address:                   123 st. ABC village...
    pass


def update_student():
    # TODO (Althea Aragon):
    # Add a function to update an existing student record.
    # - First, show the list of student records
    # - Allow the user to input the key
    # - Let the user update the value of the inputted key
    #   - coordinate with (Grace Lim) for restrictions
    pass


def delete_student():
    # TODO (Hoshea Lopez):
    # Add a function to delete a student record.
    # - Show a list of student names
    # - Allow the user to input the name for the record they want to delete
    # - Confirm before deletion
    pass


def search_student(student_list):
    clear_screen()
    
    # used to track if a student info has been found
    found = False
    
    # user is allowed to search using either of the 3 values
    user_input = input("Search for a student (ID, Name, or Program): ")
    for index in range(0, len(student_list), 1):
        if (
            student_list[index]["student_id"] == user_input or
            student_list[index]["full_name"] == user_input or 
            student_list[index]["program"] == user_input
            ):
            print(
                "\n-------------------------------------------------------"
                f"\nStudent ID:     {student_list[index]['student_id']}"
                f"\nName:           {student_list[index]['full_name']}"
                f"\nProgram:        {student_list[index]['program']}"
                f"\nContact Info:   {student_list[index]['contact_number']}"
                f"\nAddress:        {student_list[index]['address']}"
                "\n-------------------------------------------------------"
                )
            found = True
            
    if found == False:
        print("student(s) does not exist")


def exit_program():
    # TODO (Grace Lim):
    # Add a function to exit the program.
    # - Optionally confirm exit before quitting
    pass

def main():
    
    # TODO Change the layout of the menu
    clear_screen()
    print("STUDENT RECORDS SYSTEM")
    print("")
    print("MENU"
          "\n1. List All Students"
          "\n2. Add New Student"
          "\n3. Update a Student Record"
          "\n4. Delete a Student Record"
          "\n5. Search Student"
          "\n6. Exit")
    print("")
    user_input = int(input("Enter Choice (1-6): "))
    
    match user_input:
        case 1:
            list_students()
        case 2:
            add_student()
        case 3:
            update_student()
        case 4:
            delete_student()
        case 5:
            search_student()
        case 6:
            exit_program()

    
main()