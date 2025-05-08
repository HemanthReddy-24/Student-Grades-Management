import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Student Grades Management", page_icon="📚", layout="centered")

# Title of the application
st.title("Student Grades Management System")
st.subheader("Login Page")

# Login form
user_type = st.radio("Login as:", ("Student", "Teacher"))

username = st.text_input("Username", placeholder="Enter your Student ID or Teacher ID")
password = st.text_input("Password", type="password", placeholder="Enter your default password")

if st.button("Login"):
    if username and password:
        # Placeholder for authentication logic
        st.success(f"Welcome, {user_type}!")
    else:
        st.error("Please enter both username and password.") 
        