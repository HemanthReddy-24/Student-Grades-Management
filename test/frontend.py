# frontend.py
import streamlit as st
from backend import class_report, manage_marks, manage_students

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
