class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def update_contact(self, phone=None, email=None, address=None):
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address

    def display_contact(self):
        print(f"Name:- {self.name}")
        print(f"Phone:- {self.phone}")
        print(f"Email:- {self.email}")
        print(f"Address:- {self.address}")
        print('-' * 30)


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name:- ")
        phone = input("Enter phone number:- ")
        email = input("Enter email:- ")
        address = input("Enter address:- ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully!\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found!\n")
            return
        print("\nContact List:- ")
        for contact in self.contacts:
            contact.display_contact()

    def search_contact(self):
        search_term = input("Enter name or phone number to search:- ")
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone:
                contact.display_contact()
                found = True
        if not found:
            print("Contact not found!\n")

    def update_contact(self):
        name = input("Enter the name of the contact to update:- ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                phone = input(f"Enter new phone (current:- {contact.phone}):- ")
                email = input(f"Enter new email (current:- {contact.email}):- ")
                address = input(f"Enter new address (current:- {contact.address}):- ")
                contact.update_contact(phone, email, address)
                print("Contact updated successfully!\n")
                return
        print("Contact not found!\n")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete:- ")
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!\n")
                return
        print("Contact not found!\n")


def display_menu():
    print("\nContact Book Menu:- ")
    print("1. Add Contact.")
    print("2. View Contacts.")
    print("3. Search Contact.")
    print("4. Update Contact.")
    print("5. Delete Contact.")
    print("6. Exit!")


def main():
    contact_book = ContactBook()
    while True:
        display_menu()
        choice = input("Choose an option:- ")

        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.search_contact()
        elif choice == '4':
            contact_book.update_contact()
        elif choice == '5':
            contact_book.delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
