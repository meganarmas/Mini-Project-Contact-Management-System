import re
import os

def add_contact():
    contact_name = input("Enter contact's name: ")
    contact_number = input("Enter contact's phone number: ")
    contact_email = input("Enter contact's email address: ")
    additional_info = input("Enter additional information. If none, type 'N/A': ")
    contact_infos = {'name': contact_name, 'phone number': contact_number, 'email': contact_email, 'additonal information': additional_info}
    print(f"{contact_infos} has been added.")

def editing_contact():
    edit_contact_info = input("Enter the name of the contact you would like to edit: ")

def delete_contact( contact_infos):
    contact_info = input("What is the name of the contact you would like to delete: ")
    if contact_info in contact_infos:
         del contact_infos
         print("Contact was deleted.")
    else:
        print("User was not found.")
         
     
def search_contact():
    pass

def display_contacts(contact_infos):
    print("All contacts:")
    for contact_name, contact_number, contact_email in contact_infos:
        print(f"\n Name: {contact_name}")
        print(f"\n Phone number: {contact_number}")
        print(f"\n Email: {contact_email}")
    else:
        print("Contact not found.")



def export_contacts(filename):
    export_answer = input("Name of text file to export contacts to: ")
    try:
        with open('export_file.txt', 'w') as file:
            for contact_info in contact_infos:
                file.write(contact_info)
    except FileNotFoundError:
        print("Error in file. Please check the file before continuing.")

def import_contacts(filename):
    user = input("Name of text file to import contacts list to: ")
    try:
        with open('import_contacts_to_text_file', 'r'):

    else FileNotFoundError:
        print("Import file not found.")
    except FileExistsError:
        print("Error in file. Please check the file before continuing.")

def main():
    while True:
        print("Welcome to the Contact Management System! \n Menu")
        print("1. Add a new contact.")
        print("2. Edit an existing contact.")
        print("3. Delete a contact.")
        print("4. Search for a contact.")
        print("5. Display all contacts.")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")
        choice = input("Enter choice: ")
            
        if choice == '1':
            print("Preparing to add new contact....")
            add_contact()   
        elif choice == '2':
            print("Editing contact information.")
            editing_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts(filename)
        elif choice == '7':
            import_contacts(filename)
        elif choice == '8':
            print("Thank you for using the Contact Management System! Closing now.")
            break
        else:
            print("Invalid choice. Please select a number from 1 - 8.")    

if __name__ == "__main__":
    main()