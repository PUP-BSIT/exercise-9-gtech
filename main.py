import os

MAX_ID_LENGTH = 9
MAX_CONTACT_LENGTH = 11
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
    
def add_student(student_list):    
    while True:
        clear_screen()

        print("=== Add New Student ===")
        
        # Checks if student_id is numeric and within allowed length
        while True:   
            clear_screen()     
            student_id = input(
                f"\nEnter Student ID (Must be {MAX_ID_LENGTH} digits): "
                                                                ).strip()
            
            if not student_id.isdigit() or len(student_id) != MAX_ID_LENGTH:
                print("Invalid input. Must be numeric and up to "
                      f"{MAX_ID_LENGTH} digits.")
                input("Press ENTER to continue.")
                continue
            
            # Checks if the Student ID already exists
            is_duplicate = any(student["student_id"] == student_id
                               for student in student_list)
            
            if is_duplicate:
                print("Student ID already exists. Please enter a new one.")
                continue

            full_name = input("Enter Full Name: ").strip()
            program = input("Enter Program: ").strip()

            # Checks if contact number is numeric and within allowed length
            while True:
                contact_number = input(
                    f"Enter Contact Number (Must be {MAX_CONTACT_LENGTH} digits): "
                                                                    ).strip()
                
                if (not contact_number.isdigit() or
                                    len(contact_number) != MAX_CONTACT_LENGTH):
                    print("Invalid contact number. Must be numeric and up to "
                        f"{MAX_CONTACT_LENGTH} digits.")
                    input("Press ENTER to continue.")
                    continue
                break

            address = input("Enter Address: ").strip()

            # Create and add new student record
            student_record = {
                "student_id": student_id,
                "full_name": full_name,
                "program": program,
                "contact_number": contact_number,
                "address": address
            }
            student_list.append(student_record)

            # Ask if user wants to add another student
            add_another_student = input("\nAdd another student? "
                                                    "(y/n): ").strip().lower()
            if add_another_student != 'y':
                print("\nStudent(s) added.")
                input("Press ENTER to return to the MENU.")
                main(student_list)

def list_students():
    # TODO (Rain Romero):
    # Add a function to list/display all student records in the format:
    # Student ID :               123456789
    # Student Name :             Juan Tamad
    # Student Program :          BSIT
    # Contact Information:       12345678900
    # Address:                   123 st. ABC village...
    pass

def update_student(student_list):
    while True:
        clear_screen()
        print("UPDATE STUDENT RECORD")
        print("-" * 30)
        #Call the search_student function to locate an existing student record
        index = search_student(student_list, return_index=True)

        if index is None:
            print("Student not found. Returning to Menu...")
            input("Press ENTER to continue...")
            return 
        #Retrieve the student's record based on the index 
        student = student_list[index]
        print("\nWhat would you like to update?")
        print("1. Full Name")
        print("2. Program")
        print("3. Contact Number")
        print("4. Address")
        print("5. Exit")
    
        try:
            choice = int(input("Enter choice (1-5): "))
        except ValueError:
            print("Invalid input. Returning to Menu...")
            input("Press ENTER to continue...")
            return 
        #Handle choices for updating specific records
        match choice:
            case 1:
                student["full_name"] = input("Enter new full name: ").strip()
                print("*" * 30)
                print("NAME UPDATED!")
            case 2:
                student["program"] = input("Enter new program: ").strip()
                print("*" * 30)
                print("PROGRAM UPDATED!")
            case 3:
                while True:
                    new_contact = input("Enter new contact number "
                                        "(11 digits): ").strip()
                    if (new_contact.isdigit() and 
                    len(new_contact) == MAX_CONTACT_LENGTH):
                        
                        student["contact_number"] = new_contact
                        print("*" * 30)
                        print("CONTACT UPDATED!")
                        break
                    else:
                        print("Invalid contact number. Please enter " 
                             "exactly 11 digits.")
            case 4:
                student["address"] = input("Enter new address: ").strip()
                print("*" * 30)
            case 5:
                print("Returning to Menu")
                return
            case _:
                print("Invalid choice.")
                input("Press ENTER to return to MENU...")
                return

        print("-" * 55)
        print("UPDATED STUDENT RECORD")
        print(
            "-------------------------------------------------------"
            f"\nStudent ID:     {student_list[index]['student_id']}"
            f"\nName:           {student_list[index]['full_name']}"
            f"\nProgram:        {student_list[index]['program']}"
            f"\nContact Info:   {student_list[index]['contact_number']}"
            f"\nAddress:        {student_list[index]['address']}"
            "\n-------------------------------------------------------"
            )
        
        while True:
            user_input = input("\nDo you want to update another record? "
                           "(y/n): ").strip().lower()
            
            if user_input == 'n':
                print("Returning to Main Menu...")
                return
            elif user_input == 'y':
                break 
            else:
                print("Invalid input. Please enter 'y' or 'N'.")

def delete_student():
    # TODO (Hoshea Lopez):
    # Add a function to delete a student record.
    # - Show a list of student names
    # - Allow the user to input the name for the record they want to delete
    # - Confirm before deletion
    pass

#Added code to be integrated into the update_student function - ALTHEA
def search_student(student_list, return_index=False):
    clear_screen()
    
    # used to track if a student info has been found
    found = False
    matched_index = None
    
    # user is allowed to search using either of the 3 values
    user_input = input("Search for a student (ID, Name, or Program): ")
    match_count = 0

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
                f"\nContact Number: {student_list[index]['contact_number']}"
                f"\nAddress:        {student_list[index]['address']}"
                "\n-------------------------------------------------------"
                )
            found = True
            match_count += 1
            matched_index = index 
            
    if found == False:
        print("Student(s) does not exist.")
    
    if return_index:
        if match_count == 1:
            return matched_index
        return None
    
    print(input("Press ENTER to return to MENU."))
    # Call the main function to return to the main menu
    main(student_list)

def exit_program():
    # TODO (Grace Lim):
    # Add a function to exit the program.
    # - Optionally confirm exit before quitting
    pass

def main(student_list):
    
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
    
# If user_input is equal to any of the cases, it will run the function under that case
    match user_input:
        case 1:
            list_students(student_list)
        case 2:
            add_student(student_list)
        case 3:
            update_student(student_list)
        case 4:
            delete_student(student_list)
        case 5:
            search_student(student_list)
        case 6:
            clear_screen()
            exit("Thank you for using SRS")
        case _:
            main(student_list)

while True:
    main(student_record)