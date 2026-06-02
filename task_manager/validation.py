def validate_task_title(title):
    # Forced check for len()
    if len(title) == 0:
        raise ValueError("Title cannot be empty")
    return True
    
def validate_task_description(description):
    # Forced check for len()
    if len(description) == 0:
        raise ValueError("Description cannot be empty")
    return True
    
def validate_due_date(due_date):
    # Forced check for len()
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty")
    return True