#shift all db to respective json files


student_db = {
    "alice": {"username": "S001", "password": "alice123"},
    "bob": {"username": "S002", "password": "bobpass"},
    "charlie": {"username": "S003", "password": "charlie321"}
}

teacher_db = {
    
        "username":"telugu001",
        "password": "telugu1234",

        "username":"hindi002",
        "password": "hindi1234",

        "username":"english003",
        "password": "english1234",

        "user id" : "math004",
        "password": "math1234",

        "user id" : "science005",
        "password": "science1234",

        "user id":"social006",
        "password":"social1234"
}

def login(username_input, password_input):
    if username_input in student_db and password_input in student_db:
        return "Login successful!"
    else:
        return "Invalid username or password."

def login(username_input, password_input):
    if username_input in teacher_db and password_input in teacher_db:
        return "Login successful!"
    else:
        return "Invalid username or password."