# Simple phonebook application version 2 using match case
#
# Author: Gurnoor Singh Saini

phonebook = {}

def add_contact(name, number):
    phonebook[name] = number
    print(f"Contact '{name}' with number '{number}' added successfully.\n")

def search_contact(name):
    if name in phonebook:
        print(f"Contact '{name}' found, Number: {phonebook[name]}\n")
    else:
        print(f"Contact '{name}' not found.\n")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted successfully.\n")
    else:
        print(f"Contact '{name}' not found.\n")

def show_contacts():
    if not phonebook:
        print("Phone book is empty.\n")
    else:
        print("Phonebook Contacts:")
        for name, number in phonebook.items():
            print(f"Name: {name}, Number: {number}\n")

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Show all contacts")
    print("4. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number (10 digits only): ")
            add_contact(name, number)
        case "2":
            name = input("Enter contact name: ")
            search_contact(name)
        case "3":
            name = input("Enter contact name: ")
            delete_contact(name)
        case "4":
            show_contacts()
        case "5":
            print("Exiting program...")
            exit()
        case _:
            print("Invalid choice. Please try again.")