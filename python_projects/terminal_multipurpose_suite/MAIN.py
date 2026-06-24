
from tasks.task_manager import TaskManager

task_manager = TaskManager()

while True:

    try:
        print("1 - add task")
        print("2 - view task")
        print("3 - complete task")
        print("4 - delete task")
        print("E - exit\n")
        option = input("\nEnter your option : ").lower()
        if option == "1":
            title = input("\nEnter your task title : ").lower()
            task_manager.add_task(title)
            print("\nTask added successfully")
        elif option == "2":
            print(task_manager.list_tasks())
        elif option == "3":
            task_id = int(input("\nEnter your task id : "))
            result = task_manager.complete_task(task_id)
            print(result)
        elif option == "4":
            task_id = int(input("\nEnter your task id : "))
            task_manager.delete_task(task_id)
            print(f"\nTask {task_id} deleted successfully")
        elif option == "e":
            break
        else:
            print("Invalid option")
    except ValueError:
        print("Invalid option")




