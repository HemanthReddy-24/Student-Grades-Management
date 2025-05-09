import streamlit as st

# Page settings
st.set_page_config(page_title="Change Password", layout="centered")

# Title
st.markdown("## 🔒 Change Your Password")

# Inputs
old_password = st.text_input("Enter your old password", type="password")
new_password = st.text_input("Enter your new password", type="password")
confirm_password = st.text_input("Confirm your new password", type="password")

# Submit button
st.button("Change Password")