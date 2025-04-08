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
    add_another_student = "yes"
    
    while add_another_student == "yes":
        clear_screen()
        print("=== ADD NEW STUDENT RECORD ===")
        
        # Checks if student_id is numeric and within allowed length   
        student_id = input("\nEnter Student ID"
                           f"(Must be {MAX_ID_LENGTH} digits): ").strip()
            
        if not student_id.isdigit() or len(student_id) != MAX_ID_LENGTH:
            print("Invalid input. Must be numeric and "
                  f"up to {MAX_ID_LENGTH} digits.")
            input("Press ENTER to continue.")
            continue
        
        # Checks if the Student ID already exists
        is_duplicate = any(student["student_id"] == student_id for 
                           student in student_list)
            
        if is_duplicate:
            print("Student ID already exists. Please enter a new one.")

        full_name = input("Enter Full Name: ").strip()
        program = input("Enter Program: ").strip()

        # Checks if contact number is numeric and within allowed length
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
                                        "student? (yes/no): ").strip().lower()
            
            if add_another_student == 'no':
                print("\nStudent(s) added.")
                print(input("Press ENTER to return to MENU."))
                return
            elif add_another_student == 'yes':
                break 
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")   

def list_students(student_list):
        clear_screen()
        print("=== STUDENT RECORD LIST ===\n")
        
         # Check if the list is empty
        if not student_list:
             print("No student records available.")
        else:
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
    while True:
        clear_screen()
        print("=== UPDATE STUDENT RECORD ===")
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
        print("=== UPDATED STUDENT RECORD ===")
        print(
            "-------------------------------------------------------"
            f"\nStudent ID:     {student_list[index]['student_id']}"
            f"\nName:           {student_list[index]['full_name']}"
            f"\nProgram:        {student_list[index]['program']}"
            f"\nContact Number:   {student_list[index]['contact_number']}"
            f"\nAddress:        {student_list[index]['address']}"
            "\n-------------------------------------------------------"
            )
        
        while True:
            update_another_record = input("\nDo you want to update another "
                                          "record? (yes/no): ").strip().lower()
            
            if update_another_record == 'no':
                print(input("Press ENTER to return to MENU."))
                return
            elif update_another_record == 'yes':
                break 
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


def delete_student(student_list):
    clear_screen()
    print("=== DELETE STUDENT RECORD ===")
    print("-" * 30)

    if not student_list:
        print("No student records to delete.")
        input("Press ENTER to return to menu...")
        return

    # Display all student records
    print("List of Students:")
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
            print(f"ID: {matched_student['student_id']}")

            confirm = input("Are you sure you want to delete"
                            " this student? (yes/no): ").strip().lower()
            if confirm == "yes":
                student_list.remove(matched_student)
                delete_student_choice = input(f"Student record "
                    "deleted successfully. Do you want to "
                    "delete a record again? (yes/no): ").strip().lower()
                if delete_student_choice == "yes":
                        continue
                elif delete_student_choice == "no":
                        print(input("Press ENTER to return to MENU."))
                        break
                else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
            else:
                delete_student_choice = input(f"Student record "
                    "deleted successfully. Do you want to "
                    "delete a record again? (yes/no): ").strip().lower()
                if delete_student_choice == "yes":
                    continue
                elif delete_student_choice == "no":
                    print(input("Press ENTER to return to MENU."))
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")


def search_student(student_list, return_index=False):
    search_another_student = "yes"
    
    while search_another_student == "yes": 
        clear_screen()
        print("=== SEARCH STUDENT RECORD ===")
        print("-" * 30)
        
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

        while True:
            search_another_student = input("\nDo you want to search another "
                                          "record? (yes/no): ").strip().lower()
            
            if search_another_student == 'no':
                print(input("Press ENTER to return to MENU."))
                return
            elif search_another_student == 'yes':
                break 
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

def main(student_list):
    
# TODO Change the layout of the menu
    clear_screen()
    print("***** STUDENT RECORDS SYSTEM *****")
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