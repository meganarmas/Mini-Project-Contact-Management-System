def add_contact():
    print("Put name in here.")
    contact_name = input("Enter contact's name: ")
    contact_number = input("Enter contact's phone number: ")
    contact_email = input("Enter contact's email address: ")
    additional_info = input("Enter additional information. If none, type 'N/A': ")
    contact_infos = {'name': contact_name, 'phone number': contact_number, 'email': contact_email, 'additonal information': additional_info}
    print(f"{contact_infos} has been added.")


add_contact()