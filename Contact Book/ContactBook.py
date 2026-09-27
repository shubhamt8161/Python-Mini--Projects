Contacts ={}

while True:
    print("\n1. Add contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice =input("Enter your Choice: ")
    if choice =="1":
        name = input("Enter your Name: ")
        number = input("Enter your Number: ")
        print("Name",name)
        print("Number",number)
        Contacts[name]=number
        print("Contact Added!")

    elif choice =="2":
        print("All Contacts: ")
        for names, number in Contacts.items():
            print("-",names ,number)


    elif choice =="3":
        s1 = input("Enter the name to search:")
        if s1 in Contacts:
            print("Name",s1)
            print("Number:",Contacts[s1])
        else:
            print("Not Found!")

    elif choice =="4":
        s2 = input("Enter the contact you want to delete!:")
        if name in Contacts:
            Contacts.pop(name)
            print("Contact deleted!")
        else:
            print("Contact not Found!")

    elif choice =="5":
        print("Goodbye!")
        break

    




