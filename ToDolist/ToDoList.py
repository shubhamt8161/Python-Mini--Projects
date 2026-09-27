tasks = []
completed_tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Mark Tasks as Completed")
    print("5. Exit")


    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for task in tasks:
            print("-", task)
        
        print("\nCompleted Tasks:")
        for task in completed_tasks:
            print("✓", task)

    elif choice =="3":
        task =input("Enter the task you want to delete: ")
        if task in tasks:
            tasks.remove(task)
            print("Task deleted")
        else:
            print("Soory not Found!")


    elif choice == "4":
        task = input("Enter the task you completed: ")

        if task in tasks:
            tasks.remove(task)
            completed_tasks.append(task)
            print("Task completed!")
        else:
            print("Task not found!")


    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice!")
