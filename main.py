import os

MAX_ID_LENGTH = 9
MAX_CONTACT_LENGTH = 11

# list of dictionaries
student_record = []

def clear_screen():
    os.system('cls')
    os.system('clear')
    
def add_student(student_list):    
    add_another_student = "y"
    
    while add_another_student == "y":
        clear_screen()
        print("*" * 65)
        print("\t\t=== ADD NEW STUDENT RECORD ===")
        print("*" * 65)
        
        # Checks if student_id is numeric and within allowed length   
        student_id = input("\nEnter Student ID"
                           f" (Must be {MAX_ID_LENGTH} digits): ").strip()
            
        if not student_id.isdigit() or len(student_id) != MAX_ID_LENGTH:
            print("Invalid input. Must be numeric and "
                  f"up to {MAX_ID_LENGTH} digits.")
            input("Press ENTER to continue.")
            continue
        
        # Checks if any student in the student_list has a matching student_id
        is_duplicate = any(student["student_id"] == student_id for 
                           student in student_list)
            
        if is_duplicate:
            print(input("Student ID already exists. Please enter a new one."))
            input("Press ENTER to continue")
            continue

        full_name = input("Enter Full Name: ").strip()
        program = input("Enter Program: ").strip()

        # Checks if contact_number is numeric and within allowed length
        while True:
            contact_number = input(f"Enter Contact Number (Must be "
                                   f"{MAX_CONTACT_LENGTH} digits): ").strip()
                
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

        while True:
            add_another_student = input("\nDo you want to add another " 
                                        "student? (y/n): ").strip().lower()
            
            if add_another_student not in ('y', 'n'):
                print("Invalid input. Please enter 'y' or 'n'.")
                continue

            if add_another_student == 'n':
                print("\nStudent(s) added.")
                input("Press ENTER to return to MENU.")
                return 
            break 

def list_students(student_list):
    clear_screen()
    print("*" * 65)
    print("\t\t=== STUDENT RECORD LIST ===")
    print("*" * 65)
        
    # Check if the list is empty
    if not student_list:
        print("No student records available.")
    # Loop through each student in the list and print their details
    for student in student_list:
        print("----------------------------------------------------")
        print(f"Student ID:           {student['student_id']}")
        print(f"Student Name:         {student['full_name']}")
        print(f"Student Program:      {student['program']}")
        print(f"Contact Number:       {student['contact_number']}")
        print(f"Address:              {student['address']}")
        print("----------------------------------------------------")

    input("\nPress ENTER to return to the MENU.")

def update_student(student_list):
    update_another_student = "y"
    
    while update_another_student == "y":
        clear_screen()
        print("*" * 65)
        print("\t\t=== UPDATE STUDENT RECORD ===")
        print("*" * 65)
        # Call the search_student function to locate an existing student record
        index = search_student(student_list, return_index_flag=True)

        if index is None: 
            while True:
                input_again = input("\nStudent not found. Do you want to try" 
                                   " another input? (y/n): ").strip().lower()          
                if input_again == 'y':
                    break 
                elif input_again == 'n':
                    print(input("Press ENTER to return to MENU."))
                    return 
                else:
                    print("Invalid input. Please enter 'y' or 'n")
            continue  
        # Retrieve the student's record based on the index 
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
            print("Invalid input.")
            input("\nPress ENTER to continue...")
            return 
        # Handle choices for updating specific records
        match choice:
            case 1:
                case_1(student)
            case 2:
                case_2(student)
            case 3:
                case_3(student)
            case 4:
                case_4(student)
            case 5:
                return
            case _:
                input("Invalid input.")
                return
            
        print("-" * 55)
        print("\t\t=== UPDATED STUDENT RECORD ===")
        print(
            "-------------------------------------------------------"
            f"\nStudent ID:     {student_list[index]['student_id']}"
            f"\nName:           {student_list[index]['full_name']}"
            f"\nProgram:        {student_list[index]['program']}"
            f"\nContact Number: {student_list[index]['contact_number']}"
            f"\nAddress:        {student_list[index]['address']}"
            "\n-------------------------------------------------------"
            )
        # Prompt the user if they want to update another student record
        while True:
            update_another_record = input("\nDo you want to update another "
                                          "record? (y/n): ").strip().lower()
            
            if update_another_record == 'n':
                print(input("Press ENTER to return to MENU."))
                return
            elif update_another_record == 'y':
                break 
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

def case_1(student):
    clear_screen()
    student["full_name"] = input("Enter new full name: ").strip()
    print("-" * 55)
    print("NAME UPDATED!")
    
def case_2(student):
    clear_screen()
    student["program"] = input("Enter new program: ").strip()
    print("-" * 55)
    print("PROGRAM UPDATED!")
    
def case_3(student):
    while True:
        new_contact = input("Enter new contact number "
                            "(11 digits): ").strip()
        if (new_contact.isdigit() and 
            len(new_contact) == MAX_CONTACT_LENGTH):
            clear_screen()
            student["contact_number"] = new_contact
            print("-" * 55)
            print("CONTACT UPDATED!")
            break
        else:
            print("Invalid contact number. Please enter " 
                    "exactly 11 digits.")
        
def case_4(student):
    clear_screen()
    student["address"] = input("Enter new address: ").strip()
    print("-" * 55)
    print("ADDRESS UPDATED!")

def delete_student(student_list):
    clear_screen()
    print("*" * 65)
    print("\t\t\t=== DELETE STUDENT RECORD ===")
    print("*" * 65)

    if not student_list:
        print("No student records to delete.")
        input("Press ENTER to return to MENU.")
        return

    # Display all student records
    print ("-" * 65)
    print("\t\t\t=== LIST OF STUDENTS ===")
    print ("-" * 65)
    for student in student_list:
        print(f"- {student['full_name']}")

    # Loop until a valid student name is an existing record
    while True:
        selection = input("\nEnter the full name of the "
                          "student you want to delete: ").strip()

        matched_student = None
        for student in student_list:
            if student['full_name'].lower() == selection.lower():
                matched_student = student
                break

        if matched_student:
            print("\nSelected student:")
            print(f"Name: {matched_student['full_name']}")
            print(f"ID:   {matched_student['student_id']}")

            while True:
                confirm = input("Are you sure you want to delete"
                                " this student? (y/n): ").strip().lower()
                if confirm == "y":
                    student_list.remove(matched_student)
                    while True:
                        delete_student_choice = input(f"Student record "
                            "deleted successfully. Do you want to "
                            "delete a record again? (y/n): ").strip().lower()
                        if delete_student_choice == "y":
                            continue
                        elif delete_student_choice == "n":
                            print(input("Press ENTER to return to MENU."))
                            return
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                elif confirm == 'n':
                    while True:
                        delete_student_choice = input(f"Student record "
                            "deletion withdrawn. Do you want to "
                            "delete a record again? (y/n): ").strip().lower()
                        if delete_student_choice == "y":
                            continue
                        elif delete_student_choice == "n":
                            print(input("Press ENTER to return to MENU."))
                            return
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        else: # For non-existing student records
            while True:
                delete_student_choice = input(f"Student record "
                    "does not exist. Do you want to enter an exisiting "
                    "record to delete? (y/n): ").strip().lower()
                if delete_student_choice == "y":
                    break
                elif delete_student_choice == "n":
                    print(input("Press ENTER to return to MENU."))
                    return
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

def search_student(student_list, return_index_flag=False):
    search_another_student = "y"
    
    while search_another_student == "y": 
        clear_screen()
        print("*" * 65)
        print("\t\t=== SEARCH STUDENT RECORD ===")
        print("*" * 65)
        
        # used to track if a student info has been found
        is_found = False
        matched_index = None
        
        user_input = input("Search for a student (ID or Name): ")
        match_count = 0

        for index in range(0, len(student_list), 1):
            if (
                student_list[index]["student_id"] == user_input or
                student_list[index]["full_name"] == user_input
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
                is_found = True
                match_count += 1
                matched_index = index 
                
        if is_found == False:
            print("Student(s) does not exist.")
        
        if return_index_flag:
            if match_count == 1:
                return matched_index
            return None

        while True:
            search_another_student = input("\nDo you want to search another "
                                          "record? (y/n): ").strip().lower()
            
            if search_another_student == 'n':
                print(input("\nPress ENTER to return to MENU."))
                return
            elif search_another_student == 'y':
                break 
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

def main(student_list):
    
    clear_screen()
    print("*" * 60)
    print("\t\t=== STUDENT RECORDS SYSTEM ===")
    print("*" * 60)
    print("\t\t\t MAIN MENU"
          "\n------------------------------------------------------------"
          "\n1. List All Students"
          "\n2. Add New Student"
          "\n3. Update a Student Record"
          "\n4. Delete a Student Record"
          "\n5. Search Student"
          "\n6. Exit"
          "\n------------------------------------------------------------")
    user_input = int(input("Enter Choice (1-6): "))
    
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
            exit("Thank you for using SRS!")
        case _:
            main(student_list)

while True:
    main(student_record)