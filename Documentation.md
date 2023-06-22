# **Console Based Contact Book Management System Using Python Documentation**

## **Introduction**

The Contact Book Management System is a Python-based application that allows users to manage their contacts efficiently. It provides features to add, search, view, update, and delete contacts. This documentation provides an overview of the system's functionality, installation instructions, and usage guidelines.

## **Features:**
Add Contact: Users can add new contacts by providing their name, phone number, and email address.
Search Contact: Users can search for a specific contact by entering the contact's name.
View All Contacts: Users can view all contacts stored in the contact book.
Update Contact: Users can update the phone number or email address of an existing contact.
Delete Contact: Users can delete a contact from the contact book.

## **System Requirements:**

1. Python 3.x installed on the system.
2. The pickle module is required for data serialization.
3. Any Python IDE or any other IDE with support for Python.

## **Installation:**

1. Clone the project repository from GitHub: [GitHub Repository Link](https://www.google.com "Google's Homepage")
2. Ensure Python 3.x is installed on your system.
3. Install the required dependencies by running the following command:

```python
pip install pickle
```

4. Navigate to the project directory.
5. Launch the Contact Book Management System by running the following command:

```python
python main.py
```
## **Usage:**
1. Launch the Contact Book Management System by following the installation instructions.
2. The system will display a menu with different options.
3. Choose an option by entering the corresponding number and press Enter.
4. Follow the on-screen prompts to perform the selected operation:
   - To add a contact, provide the contact's name, phone number, and email address.
   - To search for a contact, enter the contact's name.
   - To view all contacts, select the corresponding option.
   - To update a contact, enter the contact's name and provide the updated phone number or email address.
   - To delete a contact, enter the contact's name.
5. After each operation, the system will provide appropriate feedback and return to the main menu.
6. To exit the system, select the "Exit" option from the main menu.

```python
------ Contact Book ------
1. Add Contact
2. Search Contact
3. View All Contacts
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 1

Enter contact name: John Doe
Enter contact phone number: 1234567890
Enter contact email: john.doe@example.com

Contact added successfully!

------ Contact Book ------
1. Add Contact
2. Search Contact
3. View All Contacts
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 2

Enter the name of the contact: John Doe

Name: John Doe
Phone: 1234567890
Email: john.doe@example.com

------ Contact Book ------
1. Add Contact
2. Search Contact
3. View All Contacts
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 3

Name: John Doe
Phone: 1234567890
Email: john.doe@example.com

------ Contact Book ------
1. Add Contact
2. Search Contact
3. View All Contacts
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 4

Enter the name of the contact: John Doe
Current contact information:
Name: John Doe
Phone: 1234567890
Email: john.doe@example.com

Enter updated phone number (leave blank to keep current): 9876543210
Enter updated email (leave blank to keep current):

Contact updated successfully!

------ Contact Book ------
1. Add Contact
2. Search Contact
3. View All Contacts
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 5

Enter the name of the contact: John Doe

Contact deleted successfully!

------ Contact Book ------
1. Add Contact
2. Search Contact
3. View All Contacts
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 6
```

## **Conclusion:**
The Contact Book Management System is a simple yet effective tool for managing contacts. By following the installation instructions and usage guidelines provided in this documentation, users can easily add, search, view, update, and delete contacts as needed. Feel free to explore and enhance the system further according to your requirements.

For detailed implementation and code understanding, please refer to the source code files in the project repository.
