expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Delete Expense")
    print("5. Exit")

    choice=input("Enter your Choice: ")
    if choice=="1":
        expense = float(input("Enter expense amount: "))
        expenses.append(expense)
        print("Expense added!")

    elif choice == "2":
        print("\nYour Expenses:")
        for expense in expenses:
            print("-",expense)

    elif choice == "3":
        total =sum(expenses)
        print("Total:",total)

    elif choice == "4":
        expense =float(input("Enter your Expense to delete:"))
        if expense in expenses:
            expenses.remove(expense)
            print("Expense deleted!")
        else:
            print("Expense not Found!")

    elif choice == "5":
        print("Goodbye!")
        break

