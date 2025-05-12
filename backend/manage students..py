# Add a new student
def add_student(name, email, dob, enrollment_year):
    data = load_data()
    new_id = max([s['student_id'] for s in data['students']], default=0) + 1
    new_student = {
        "student_id": new_id,
        "name": name,
        "email": email,
        "dob": dob,
        "enrollment_year": enrollment_year
    }
    data['students'].append(new_student)
    save_data(data)
    print(f"✅ Added: {new_student}")

# Update an existing student's information
def update_student(student_id, updated_fields):
    data = load_data()
    for student in data['students']:
        if student['student_id'] == student_id:
            student.update(updated_fields)
            save_data(data)
            print(f"✅ Updated Student {student_id}")
            return
    print(f"❌ Student ID {student_id} not found.")

# Delete a student by ID
def delete_student(student_id):
    data = load_data()
    new_students = [s for s in data['students'] if s['student_id'] != student_id]
    if len(new_students) == len(data['students']):
        print(f"❌ Student ID {student_id} not found.")
        return
    data['students'] = new_students
    save_data(data)
    print(f"🗑️ Deleted Student ID {student_id}")

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"students": []}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# ✅ Teacher: Add or update marks
def add_or_update_marks(student_id, subject_marks):
    data = load_data()
    for student in data['students']:
        if student['student_id'] == student_id:
            if "marks" not in student:
                student["marks"] = {}
            student["marks"].update(subject_marks)
            save_data(data)
            print(f"✅ Marks updated for Student ID {student_id}")
            return
    print(f"❌ Student ID {student_id} not found.")

# ✅ Student: View marks in tabular format
def view_marks(student_id):
    data = load_data()
    for student in data['students']:
        if student['student_id'] == student_id:
            marks = student.get("marks", {})
            if not marks:
                print("📄 No marks available yet.")
                return
            print(f"\n📊 Marks for {student['name']}:")
            print("----------------------")
            print("| Subject    | Marks |")
            print("----------------------")
            for subject, score in marks.items():
                print(f"| {subject:<10} | {score:<5} |")
            print("----------------------")
            return
    print(f"❌ Student ID {student_id} not found.")