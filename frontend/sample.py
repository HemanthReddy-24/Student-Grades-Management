import streamlit as st

# Set the title of the app
st.title("Login Page")

# Create input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Add a login button
if st.button("Login"):
    if username == "admin" and password == "password123":
        st.success("Login successful!")
    else:
        st.error("Invalid username or password") 

        print("Invalid username or password")