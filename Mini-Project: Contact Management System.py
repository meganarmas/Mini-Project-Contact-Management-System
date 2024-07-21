import re 
import os

contact_infos = []

def add_contact():
    contact_name = input("Enter contact's name: ")
    contact_number = input("Enter contact's phone number: ")
    contact_email = input("Enter contact's email address: ")
    additional_info = input("Enter additional information. If none, type 'N/A': ")
    full_contact_info = {'name': contact_name, 'phone number': contact_number, 'email': contact_email, 'additonal information': additional_info}
    contact_infos.append(full_contact_info)
    print(f"{full_contact_info} has been added.")

def editing_contact(contact_infos):
    name = input("What is the name of the person you would like edit's contact: ")
    contact_names = [{entry["name"]: contact_infos.index(entry)} for entry in contact_infos]
    for contact in contact_names:
        if name in contact:
            print("1. Name")
            print("2. Phone Number")
            print("3. Email Address")
            print("4. Additional Information")
            choice = input("What would you like to edit: ")
            
            if choice == '1':
                contact_name = input("Enter contact's new name: ")
                contact_infos[contact[name]]["name"] = contact_name
            elif choice == '2':
                contact_number = input("Enter contact's new number: ")
                contact_infos[contact[name]]["phone number"] = contact_number
            elif choice == '3':
                contact_email = input("Enter contact's new email: ")
                contact_infos[contact[name]]["email address"] = contact_email
            elif choice == '4':
                additional_info = input("Enter new additional information: ")
                contact_infos[contact[name]]["additional information"] = additional_info
    else:
        print("Contact not found.")

def delete_contact(contact_infos):
    remove_contact = input("What is the name of the contact you would like to delete: ")
    contact_names = [{entry["name"]: contact_infos.index(entry)} for entry in contact_infos]
    for contact in contact_names:
        if remove_contact in contact:
            remove_contact = contact.pop
            print("Contact was deleted.")
        else:
            print("User was not found.")

def search_contact(contact_infos):
        email_address = input("Insert email address to search for contact: ")
        email_address = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", contact_infos.index)
        if email_address in contact_infos:
            print(f"{contact_infos.index}")
        else:
            print("Contact not found.")

def display_contacts(contact_infos):
    for contact in contact_infos:
        print(f"Name: {contact["name"]}")
        print(f"Phone number: {contact["phone number"]}")
        print(f"Email: {contact["email address"]}")
    if not contact_infos:
        print("No contacts found.")

def export_contacts(file, contact_infos):
    try:
        with open('export_file.txt', 'w') as file:
            for contact in contact_infos:
                file.write(f"{contact}")
                print("Contact export completed.")
    except FileNotFoundError:
        print("Error in file. Please check the file before continuing.")

def import_contacts(file):
    try:
        with open('import_contacts.txt', 'r') as file:
            for line in file:
                contact_name, contact_number, contact_email, additonal_information = line.strip().split(',')
                contact_infos.index = {"name": contact_name, "phone number": contact_number, "email": contact_email, "additonal information": additonal_information}
                print("Contacts imported completed.")
    except FileNotFoundError:
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
            editing_contact(contact_infos)
        elif choice == '3':
            delete_contact(contact_infos)
        elif choice == '4':
            search_contact(contact_infos)
        elif choice == '5':
            display_contacts(contact_infos)
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Thank you for using the Contact Management System! Closing now.")
            break
        else:
            print("Invalid choice. Please select a number from 1 - 8.")    

if __name__ == "__main__":
    main()