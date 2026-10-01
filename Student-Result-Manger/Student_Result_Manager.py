students ={}
while True:
        print("\n -----STUDENT MANAGER APP-----")
        print("1. ADD STUDENT")
        print("2. VIEW STUDENT")
        print("3. CHECK RESULT")
        print("4. EXIT")

        choice = input("Enter your Choice: ")

        # Add student
        if choice =="1":
            name = input("Enter your Name:")
            marks=int(input("Enter Marks:"))
            students[name] = marks  # dictionary[key] = value
            print(f"{name} Sucessfully Added!")

        # View student
        elif choice =="2":
            if not students:
                print("No student Found!")
            else:
                for name , marks in students.items():
                    print(name, ":" , marks)

        # Check result
        elif choice =="3":
            name = input("Enter student name:")

            if name in students:
                marks = students[name]
                if marks >=38:
                    print("Pass")
                else:
                    print("Fail !!!!!!!")

            else:
                print("Student Not found!")


        # Exit
        elif choice =="4":
            print("Thank You!")
            break
        else:
            print("Invalid Input!")