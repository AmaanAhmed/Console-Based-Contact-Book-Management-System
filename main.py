# import the pickle module, which is used for data serialization.
import pickle

# Define the Contact class. Make sure it represents a single contact and has attributes such as name, phone, and email.
class Contact:

    # The __init__ method initializes the contact with the provided details.    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    # The __str__ method returns a string representation of the contact when it is printed.
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\n"

# Define the ContactBook class to manage a collection of contacts
class ContactBook:

    # The __init__ method initializes the contact book by loading existing contacts from the "contacts.pickle" file. 
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    # The load_contacts method attempts to load the contacts from the file using pickle.load() method.
    def load_contacts(self):
        try:
            with open("contacts.pickle", "rb") as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            pass

    # The save_contacts method saves the contacts to the "contacts.pickle" file using pickle.dump() method.
    def save_contacts(self):
        with open("contacts.pickle", "wb") as file:
            pickle.dump(self.contacts, file)

    # This method allows users to add a new contact
    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        email = input("Enter contact email: ")
        
        # Create a new Contact object with the provided details.
        contact = Contact(name, phone, email)
        # Adding it to the contacts dictionary with the name as the key.
        self.contacts[name] = contact
        # saving the updated contact book to the file.
        self.save_contacts()
        print("Contact added successfully!")

    """ The following method allows users to search for a contact by entering the contact's name.
    If the contact is found in the contacts dictionary, its details are printed.
    Otherwise, a "Contact not found!" message is displayed. """
        
    def search_contact(self):
        name = input("Enter the name of the contact: ")
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print("Contact not found!")

    """ The following method displays all the contacts stored in the contact book.
    If there are contacts in the contacts dictionary, it iterates over the values and prints each contact.
    If no contacts are found, a "No contacts found!" message is displayed. """

    def view_all_contacts(self):
        if self.contacts:
            for contact in self.contacts.values():
                print(contact)
        else:
            print("No contacts found!")

    """ This method allows users to update the phone number or email address of an existing contact.
    It prompts the user to enter the name of the contact to update. If the contact is found, its current information is displayed.
    The user can enter the updated phone number and email address. If any of the fields are left blank, the current values are retained.
    The save_contacts method is called to save the updated contact book to the file. """

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

    """ This method allows users to delete a contact from the contact book. 
    It prompts the user to enter the name of the contact to delete. 
    If the contact is found in the contacts dictionary, it is deleted using the del keyword. 
    The save_contacts method is called to save the updated contact book to the file. """
    
    def delete_contact(self):
        name = input("Enter the name of the contact: ")
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

""" This main function is the entry point of the program. 
It creates an instance of the ContactBook class to manage contacts. 
It then enters a continuous loop where it displays the menu options and handles user input until the user chooses to exit the program. """

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

 """ This block ensures that the main function is only executed when the script is run directly and not when it is imported as a module. """

if __name__ == "__main__":
    main()
