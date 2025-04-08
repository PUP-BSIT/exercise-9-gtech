# Make the code readable as it is
# add comments per block or if necessary
# make sure to avoid magic values
# add tasks and assign it to a member if there is anything else needed

# This is a sample list of dictionaries
student_record = [{
                    "student_id": "2024-00529-TG-1",
                    "full_name": "Adriel Joseph Dimayuga",
                    "program": "BSIT",
                    "contact_number": "12345678900",
                    "address": "Adriel Joseph address"
                   },
                  {
                    "student_id": "2024-00529-TG-0",
                    "full_name": "AJ",
                    "program": "BSIT",
                    "contact_number": "12345678900",
                    "address": "AJ address"
                  }]

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


def search_student():
    # TODO (Adriel Dimayuga):
    # Add a function to search for a student record.
    # - Allow searching by ID, name, or program
    # - Display matching records
    pass


def exit_program():
    # TODO (Grace Lim):
    # Add a function to exit the program.
    # - Optionally confirm exit before quitting
    pass
