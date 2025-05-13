def login(username_input, password_input):
    if username_input in "logins.json" and password_input in "logins.json":
        return "Login successful!"
    else:
        return "Invalid username or password."
    
    
def login(username_input, password_input):
    if username_input in "logins.json" and password_input in "logins.json":
        return "Login successful!"
    else:
        return "Invalid username or password."
    
    #same for teacher and student logout 
def logout():
    current = get_current_session()
    if current is not None:
        save_session(None)
        print("👋 Logged out successfully.")
    else:
        print("❌ No user is currently logged in.")
        