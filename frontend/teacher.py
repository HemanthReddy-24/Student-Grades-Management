import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

# Dummy data
students = [
    {"ID": "S001", "Name": "Alice", "GPA": 3.8, "Percentage": 95, "Marks": {"Math": 95, "Science": 90}},
    {"ID": "S002", "Name": "Bob", "GPA": 3.2, "Percentage": 80, "Marks": {"Math": 80, "Science": 75}},
    {"ID": "S003", "Name": "Charlie", "GPA": 2.8, "Percentage": 70, "Marks": {"Math": 70, "Science": 65}},
]

# Helper functions
def calculate_gpa_and_percentage(marks):
    total_marks = sum(marks.values())
    percentage = total_marks / len(marks)
    gpa = round(percentage / 25, 2)  # Assuming GPA is out of 4
    return gpa, percentage

def get_student_dataframe():
    data = []
    for student in students:
        data.append({
            "ID": student["ID"],
            "Name": student["Name"],
            "GPA": student["GPA"],
            "Percentage": student["Percentage"],
        })
    return pd.DataFrame(data)

# Page 1: Class Report
def class_report():
    st.title("Class Report")
    
    # Pie chart for pass percentage
    pass_count = sum(1 for s in students if s["Percentage"] >= 50)
    fail_count = len(students) - pass_count
    pie_chart = px.pie(
        names=["Pass", "Fail"],
        values=[pass_count, fail_count],
        title="Pass Percentage"
    )
    st.plotly_chart(pie_chart)
    
    # Bar graph for percentage ranges
    ranges = ["0-50", "51-70", "71-90", "91-100"]
    counts = [0, 0, 0, 0]
    for s in students:
        if s["Percentage"] <= 50:
            counts[0] += 1
        elif s["Percentage"] <= 70:
            counts[1] += 1
        elif s["Percentage"] <= 90:
            counts[2] += 1
        else:
            counts[3] += 1
    bar_chart = px.bar(
        x=ranges,
        y=counts,
        labels={"x": "Percentage Range", "y": "Number of Students"},
        title="Student Percentage Ranges"
    )
    st.plotly_chart(bar_chart)
    
    # Table of student details
    st.subheader("Student Details")
    df = get_student_dataframe()
    st.dataframe(df)

# Page 2: Manage Marks
def manage_marks():
    st.title("Manage Marks")
    
    # Dropdown to select subject
    subjects = list(students[0]["Marks"].keys())
    selected_subject = st.selectbox("Select Subject", subjects)
    
    # Update marks
    for student in students:
        new_marks = st.number_input(
            f"Enter marks for {student['Name']} (ID: {student['ID']})",
            value=student["Marks"][selected_subject],
            min_value=0,
            max_value=100,
        )
        student["Marks"][selected_subject] = new_marks
        student["GPA"], student["Percentage"] = calculate_gpa_and_percentage(student["Marks"])
    
    # Show updated data
    st.subheader("Updated Student Details")
    df = get_student_dataframe()
    st.dataframe(df)

# Page 3: Manage Students
def manage_students():
    global students  # <-- move this to the top
    st.title("Manage Students")
    
    # Add new student
    st.subheader("Add New Student")
    new_name = st.text_input("Name")
    new_id = st.text_input("ID")
    new_marks = {}
    for subject in students[0]["Marks"].keys():
        new_marks[subject] = st.number_input(f"Initial marks for {subject}", min_value=0, max_value=100, value=0)
    if st.button("Add Student"):
        gpa, percentage = calculate_gpa_and_percentage(new_marks)
        students.append({"ID": new_id, "Name": new_name, "GPA": gpa, "Percentage": percentage, "Marks": new_marks})
        st.success("Student added successfully!")
    
    # Delete student
    st.subheader("Delete Student")
    student_ids = [s["ID"] for s in students]
    selected_id = st.selectbox("Select Student ID to Delete", student_ids)
    if st.button("Delete Student"):
        students = [s for s in students if s["ID"] != selected_id]
        st.success("Student deleted successfully!")
# Sidebar navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Class Report", "Manage Marks", "Manage Students"])
    
    if page == "Class Report":
        class_report()
    elif page == "Manage Marks":
        manage_marks()
    elif page == "Manage Students":
        manage_students()

if __name__ == "__main__":
    main()