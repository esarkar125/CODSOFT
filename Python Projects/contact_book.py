# Define a list to store contacts (each contact is a dictionary)
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    
    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    
    contacts.append(contact)
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['Name']} - {contact['Phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    keyword = input("Enter the name or phone number to search for: ").lower()
    found_contacts = []

    for contact in contacts:
        if keyword in contact['Name'].lower() or keyword in contact['Phone']:
            found_contacts.append(contact)

    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for idx, contact in enumerate(found_contacts, 1):
            print(f"{idx}. {contact['Name']} - {contact['Phone']}")

# Function to update a contact's details
def update_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print("Contact Details:")
            for key, value in contact.items():
                print(f"{key}: {value}")
            
            print("\nEnter new details (leave blank to keep existing):")
            name = input(f"New Name ({contact['Name']}): ") or contact['Name']
            phone = input(f"New Phone ({contact['Phone']}): ") or contact['Phone']
            email = input(f"New Email ({contact['Email']}): ") or contact['Email']
            address = input(f"New Address ({contact['Address']}): ") or contact['Address']

            contacts[index] = {
                "Name": name,
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Function to delete a contact
def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted_contact = contacts.pop(index)
            print(f"{deleted_contact['Name']} - {deleted_contact['Phone']} has been deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")