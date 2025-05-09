import streamlit as st

# Page setup
st.set_page_config(page_title="Login Page", layout="centered")

st.markdown("<h1 style='text-align: center; color: lightblue;'>Student Grading System</h1>", unsafe_allow_html=True)
st.markdown("### Please choose your role")

# Role selection buttons
col1, col2 = st.columns(2)

with col1:
    student_clicked = st.button("Student", use_container_width=True)

with col2:
    teacher_clicked = st.button("Teacher", use_container_width=True)

# Input fields based on selection
if student_clicked:
    st.markdown("#### 👨‍🎓 Student Login")
    st.text_input("Student ID", key="student_id")
    st.text_input("Password", type="password", key="student_pass")
    st.button("Enter", use_container_width=True)

if teacher_clicked:
    st.markdown("#### 👩‍🏫 Teacher Login")
    st.text_input("Teacher ID", key="teacher_id")
    st.text_input("Password", type="password", key="teacher_pass")
    st.button("Enter", use_container_width=True)


