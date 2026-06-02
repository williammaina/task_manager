from .validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list globally as per the requirement
tasks = []

def add_task(title, description, due_date):
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
        task = {"title": title, "description": description, "due_date": due_date, "completed": False}
        tasks.append(task)
        print("Task added successfully!")
    
def mark_task_as_complete(index, task_list=tasks):
    # Adjusting index for 1-based user input if necessary, 
    # but assuming 0-based index based on test feedback
    if 0 <= index < len(task_list):
        task_list[index]["completed"] = True
        print("Task marked as complete!")
    
def view_pending_tasks(task_list=tasks):
    for i, task in enumerate(task_list):
        if not task["completed"]:
            print(f"{i}. {task['title']}")

def calculate_progress(task_list):
    if not task_list:
        return 0.0
    completed = [t for t in task_list if t.get("completed") == True]
    return (len(completed) / len(task_list)) * 100