#change password


def change_password(username, old_password, new_password):
    """
    Allows a student to change their password.
    - Verifies the old password first.
    - Updates to new password if valid.
    Returns:
        True if password was changed, False otherwise.
    """
    username = username.lower().strip()
    
    if username in student_db:
        if student_db[username]["password"] == old_password:
            student_db[username]["password"] = new_password
            return True
        else:
            return False  # Incorrect old password
    return False  # Student not found
