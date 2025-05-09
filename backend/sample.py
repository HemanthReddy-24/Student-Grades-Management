# backend.py

# Simulated student database (you can move to JSON later)
student_db = {
    "alice": {"username": "S001", "password": "alice123"},
    "bob": {"username": "S002", "password": "bobpass"},
    "charlie": {"username": "S003", "password": "charlie321"}
}


def add_student(username, password=None):
    """Add a new student with a username"""
    db = load_student_db()
    username = username.strip().lower()
    
    if username in db:
        return False, "Username already exists."
    
    student_id = generate_student_id()
    if not password:
        password = "default123"  # fallback default password (optional)
    
    db[username] = {
        "id": student_id,
        "password": password
    }
    save_student_db(db)
    return True, f"Student {username} added with ID {student_id}"

def remove_student(username):
    """Removes a student from the database if they exist."""
    username = username.lower().strip()
    if username in student_db:
        del student_db[username]
        return True  # Successfully removed
    return False  # Student not found

def update_student_info(username, new_id=None, new_name=None, new_age=None, new_course=None):
    username = username.lower().strip()
    if username in student_db:
        if new_id:
            student_db[username]["id"] = new_id
        if new_name:
            student_db[username]["name"] = new_name
        if new_age:
            student_db[username]["age"] = new_age
        if new_course:
            student_db[username]["course"] = new_course
        return True
    return False

