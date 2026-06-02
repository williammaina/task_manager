from task_manager import task_utils

def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter title: ")
            desc = input("Enter description: ")
            due = input("Enter due date (YYYY-MM-DD): ")
            task_utils.add_task(title, desc, due)
        elif choice == "2":
            try:
                idx = int(input("Enter index to mark complete: "))
                task_utils.mark_task_as_complete(idx)
            except ValueError:
                pass
        elif choice == "3":
            task_utils.view_pending_tasks()
        elif choice == "5":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()