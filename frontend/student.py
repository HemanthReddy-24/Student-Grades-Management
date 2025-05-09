import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Student Dashboard", layout="wide")

# Top-right corner buttons
col1, col2, col3 = st.columns([10, 1, 2])
with col2:
    st.button("Change Password")
with col3:
    st.button("Logout")

st.markdown("<h1 style='text-align: center; color: cyan;'>Student Dashboard</h1>", unsafe_allow_html=True)

# Bio section
st.markdown("## 🧬 Bio")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.text("Name: [Name]")
        st.text("Phone: [Phone Number]")
        st.text("Mother's Name: [Mother's Name]")
    with col2:
        st.text("Father's Name: [Father's Name]")
        st.text("Address: [Address]")

# Marks Table
st.markdown("## 📝 Marks")
subjects = ['Maths', 'Science', 'English', 'Social', 'Telugu', 'Hindi']
dummy_marks = [90, 85, 88, 82, 78, 91]  # Placeholder marks

df_marks = pd.DataFrame({'Subject': subjects, 'Marks': dummy_marks})
st.table(df_marks)

# Top 3 Ranks
st.markdown("## 🏆 Top 3 Ranks")
ranks = {
    "1st": "Student A - 95%",
    "2nd": "Student B - 93%",
    "3rd": "Student C - 91%",
    "Your Rank": "You - 89%"
}
for rank, info in ranks.items():
    st.markdown(f"**{rank}:** {info}")

# Graph for subject-wise performance
st.markdown("## 📊 Your Subject-wise Performance")
fig, ax = plt.subplots()
ax.bar(subjects, dummy_marks, color='skyblue')
ax.set_ylabel('Marks')
ax.set_ylim(0, 100)
ax.set_title('Performance by Subject')
st.pyplot(fig)
