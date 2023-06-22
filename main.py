import pickle

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\n"

class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        try:
            with open("contacts.pickle", "rb") as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            pass

    def save_contacts(self):
        with open("contacts.pickle", "wb") as file:
            pickle.dump(self.contacts, file)

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        contact = Contact(name, phone, email)
        self.contacts[name] = contact
        self.save_contacts()
        print("Contact added successfully!")

    def search_contact(self):
        name = input("Enter the name of the contact: ")
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print("Contact not found!")

    def view_all_contacts(self):
        if self.contacts:
            for contact in self.contacts.values():
                print(contact)
        else:
            print("No contacts found!")

    def update_contact(self):
        name = input("Enter the name of the contact: ")
        if name in self.contacts:
            contact = self.contacts[name]
            print("Current contact information:")
            print(contact)
            phone = input("Enter updated phone number (leave blank to keep current): ")
            email = input("Enter updated email (leave blank to keep current): ")
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            self.save_contacts()
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self):
        name = input("Enter the name of the contact: ")
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

def main():
    contact_book = ContactBook()

    while True:
        print("------ Contact Book ------")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.search_contact()
        elif choice == "3":
            contact_book.view_all_contacts()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

        print()

if __name__ == "__main__":
    main()
