contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search a Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        number = input("Enter phone number: ")

        contacts[name] = number
        print("Contact added")

    elif choice == 2:
        print(contacts)

    elif choice == 3:
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found")

    elif choice == 4:
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")

    elif choice == 5:
        print("Exit")
        break

    else:
        print("Invalid choice")