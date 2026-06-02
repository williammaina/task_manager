from task_manager import task_utils

def main():
    while True:
        # Note: Added simple print statements to match expected menu flow
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
        elif choice == "5":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()