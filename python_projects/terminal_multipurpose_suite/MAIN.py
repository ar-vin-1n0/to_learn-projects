from tasks.task_manager import TaskManager


manager = TaskManager()

while True:
    print("\n===== Task Manager =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("E. Exit")

    option = input("\nEnter your option: ").strip().lower()

    if option == "1":

        title = input("Enter task title: ").strip()

        manager.add_task(title)

        print("\nTask added successfully!")

    elif option == "2":

        tasks = manager.list_tasks()

        if isinstance(tasks, str):
            print(tasks)
        else:
            for task in tasks:
                print(task)

    elif option == "3":

        try:
            task_id = int(input("Enter task ID: "))

            result = manager.complete_task(task_id)

            print(result)

        except ValueError:
            print("Task ID must be a number.")

    elif option == "4":

        try:
            task_id = int(input("Enter task ID: "))

            result = manager.delete_task_by_id(task_id)

            print(result)

        except ValueError:
            print("Task ID must be a number.")

    elif option == "e":

        print("\nGoodbye!")

        break

    else:

        print("\nInvalid option. Please try again.")





