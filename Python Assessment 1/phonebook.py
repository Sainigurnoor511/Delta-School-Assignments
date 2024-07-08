# Simple phone book application (add contacts, search by name, delete contacts)
#
# Author: Gurnoor Singh Saini

phonebook = {}

def add_contact(name, number):
    phonebook[name] = number
    print("Contact added successfully!\n")

def search_contact(name):
    if name in phonebook:
        print(f"Name: {name}, Number: {phonebook[name]}\n")
    else:
        print("Contact not found!\n")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found!\n")

def show_contacts():
    if not phonebook:
        print("Phone book is empty.\n")
    else:
        print("Contacts in the phonebook:")
        for name, number in phonebook.items():
            print(f"Name: {name}, Number: {number}\n")

while True:
    print('''Choose an option:
    1. Add contact
    2. Search contact
    3. Delete contact
    4. Show all contacts
    5. Exit \n''')

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)
    elif choice == "2":
        name = input("Enter contact name: ")
        search_contact(name)
    elif choice == "3":
        name = input("Enter contact name: ")
        delete_contact(name)
    elif choice == "4":
        show_contacts()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice. Please try again.\n")