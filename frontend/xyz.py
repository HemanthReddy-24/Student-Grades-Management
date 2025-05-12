import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
 
# ----- Initialize student data -----
if 'students' not in st.session_state:
    st.session_state.students = [
        {"id": "S001", "name": "Alice Johnson", "age": 20, "course": "Computer Science", "math": 85, "science": 92, "history": 78, "english": 88},
        {"id": "S002", "name": "Bob Smith", "age": 21, "course": "Mechanical", "math": 72, "science": 68, "history": 85, "english": 79},
        {"id": "S003", "name": "Charlie Brown", "age": 22, "course": "Electrical", "math": 91, "science": 94, "history": 89, "english": 93},
        {"id": "S004", "name": "Diana Prince", "age": 20, "course": "Civil", "math": 65, "science": 70, "history": 75, "english": 68},
        {"id": "S005", "name": "Ethan Hunt", "age": 23, "course": "Computer Science", "math": 78, "science": 82, "history": 77, "english": 85}
    ]
 
# ----- Helper functions -----
def calculate_gpa_percentage(student):
    total_marks = student['math'] + student['science'] + student['history'] + student['english']
    percentage = total_marks / 4
    gpa = percentage / 25
    return round(gpa, 2), round(percentage, 2)
 
def class_report():
    st.title("📚 Class Report")
 
    students_with_gpa = []
    for student in st.session_state.students:
        gpa, percentage = calculate_gpa_percentage(student)
        students_with_gpa.append({**student, "gpa": gpa, "percentage": percentage})
   
    df = pd.DataFrame(students_with_gpa)
 
    st.subheader("Full Student List")
    st.dataframe(df)
 
    st.subheader("🏆 Top 3 Students")
    top_students = df.sort_values(by="percentage", ascending=False).head(3)
    st.table(top_students[["id", "name", "percentage", "gpa"]])
 
    st.subheader("✅ Pass Percentage")
    pass_count = df[df["percentage"] >= 40].shape[0]
    fail_count = df.shape[0] - pass_count
    fig1, ax1 = plt.subplots(figsize=(3, 3))
    ax1.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct='%1.1f%%', startangle=90, colors=["#4CAF50", "#F44336"])
    ax1.axis('equal')
    st.pyplot(fig1)
 
    st.subheader("📊 Marks Bar Graph")
    subject = st.selectbox("Select Subject", ["math", "science", "history", "english"])
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    ax2.bar(df["name"], df[subject], color='skyblue')
    ax2.set_ylabel("Marks")
    ax2.set_xlabel("Students")
    ax2.set_title(f"{subject.capitalize()} Marks")
    plt.xticks(rotation=45)
    st.pyplot(fig2)
 
def manage_marks():
    st.title("✏️ Manage Marks")
    st.subheader("Edit Marks Table")
 
    df = pd.DataFrame(st.session_state.students)
 
    subjects = ["math", "science", "history", "english"]
    marks_df = df[["id", "name"] + subjects]
 
    edited_df = st.data_editor(marks_df, num_rows="dynamic", use_container_width=True)
 
    if st.button("Save Marks Changes"):
        for idx, row in edited_df.iterrows():
            for student in st.session_state.students:
                if student['id'] == row['id']:
                    for subject in subjects:
                        student[subject] = row[subject]
        st.success("Marks updated successfully!")
 
def manage_students():
    st.title("👨‍🎓 Manage Students")
 
    st.subheader("➕ Add New Student")
    name = st.text_input("Enter Student Name")
    student_id = st.text_input("Enter Student ID")
    age = st.number_input("Enter Age", min_value=15, max_value=100)
    course = st.text_input("Enter Course")
 
    if st.button("Add Student"):
        if name and student_id and course:
            st.session_state.students.append({
                "id": student_id,
                "name": name,
                "age": age,
                "course": course,
                "math": 0,
                "science": 0,
                "history": 0,
                "english": 0
            })
            st.success(f"Student {name} added successfully!")
        else:
            st.error("Please fill all the fields.")
 
    st.subheader("➖ Remove Student")
    if len(st.session_state.students) > 0:
        remove_id = st.selectbox("Select Student ID to Remove", [s["id"] for s in st.session_state.students])
        if st.button("Remove Student"):
            st.session_state.students = [s for s in st.session_state.students if s["id"] != remove_id]
            st.success(f"Student with ID {remove_id} removed successfully!")
 
    st.subheader("✏️ Update Student Details")
    if len(st.session_state.students) > 0:
        df = pd.DataFrame(st.session_state.students)
        student_details = df[["id", "name", "age", "course"]]
        updated_details = st.data_editor(student_details, num_rows="dynamic", use_container_width=True)
 
        if st.button("Save Student Details"):
            for idx, row in updated_details.iterrows():
                for student in st.session_state.students:
                    if student['id'] == row['id']:
                        student['name'] = row['name']
                        student['age'] = row['age']
                        student['course'] = row['course']
            st.success("Student details updated successfully!")
 
# ----- Main App -----
def main():
    st.set_page_config(page_title="Student Tracking System", page_icon="🎓", layout="wide")
   
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
   
    if not st.session_state.logged_in:
        st.title("STUDENT TRACKING SYSTEM")
        st.subheader("🔑 Login Page")
 
        user_type = st.radio("Login as:", ["Student", "Teacher"], horizontal=True)
 
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
 
            if submitted:
                if not username or not password:
                    st.error("Please enter both Username and Password.")
                else:
                    st.session_state.logged_in = True
                    st.session_state.user_type = user_type.lower()
                    st.success(f"Logged in successfully as {user_type}!")
                    st.experimental_rerun()
    else:
        if st.session_state.user_type == "teacher":
            st.sidebar.title("🎓 Teacher Dashboard")
            page = st.sidebar.radio("Navigation", ["Class Report", "Manage Marks", "Manage Students"])
 
            if page == "Class Report":
                class_report()
            elif page == "Manage Marks":
                manage_marks()
            elif page == "Manage Students":
                manage_students()
        else:
            st.title("📖 Student Dashboard")
            st.info("Student view will be available soon!")
 
if __name__ == "__main__":
    main()
 