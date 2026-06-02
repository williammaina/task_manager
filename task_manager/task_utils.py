from .validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    # Call validation functions which contain the len() check
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    
    task = {"title": title, "description": description, "due_date": due_date, "completed": False}
    tasks.append(task)
    print("Task added successfully!")