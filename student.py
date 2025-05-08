import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt

# Load student data
def load_students():
    with open("student.json", "r") as f:
        return json.load(f)

# Get top 3 ranks
def get_top_students(data):
    student_scores = []
    for sid, info in data.items():
        total = sum(info["marks"].values())
        student_scores.append((sid, info["name"], total))
    top_students = sorted(student_scores, key=lambda x: x[2], reverse=True)
    return top_students[:3], {sid: rank+1 for rank, (sid, _, _) in enumerate(top_students)}

# Main app
def student_dashboard():
    st.set_page_config(page_title="Student Dashboard", layout="wide")
    
    # Check login
    if "student_id" not in st.session_state:
        st.warning("Please log in first.")
        st.stop()

    student_id = st.session_state["student_id"]
    data = load_students()

    if student_id not in data:
        st.error("Student ID not found.")
        st.stop()

    student = data[student_id]

    # Header and Logout
    col1, col2 = st.columns([9, 1])
    with col1:
        st.title("🎓 Student Dashboard")
    with col2:
        if st.button("Logout"):
            st.session_state.pop("student_id", None)
            st.experimental_rerun()

    st.subheader("📌 Bio Details")
    bio_cols = st.columns(3)
    bio_cols[0].markdown(f"**Name:** {student['name']}")
    bio_cols[0].markdown(f"**Phone:** {student['phone']}")
    bio_cols[1].markdown(f"**Father Name:** {student['father_name']}")
    bio_cols[1].markdown(f"**Mother Name:** {student['mother_name']}")
    bio_cols[2].markdown(f"**Address:** {student['address']}")

    # Marks table
    st.subheader("📝 Marks Table")
    marks = student["marks"]
    subjects = list(marks.keys())
    scores = list(marks.values())
    df = pd.DataFrame({
        "Subject": subjects,
        "Marks": scores
    })
    st.table(df)

    # Top 3 ranks
    st.subheader("🏆 Class Top 3")
    top_3, rank_dict = get_top_students(data)
    top_df = pd.DataFrame(top_3, columns=["ID", "Name", "Total Marks"])
    st.dataframe(top_df, use_container_width=True)

    # Student rank
    student_rank = rank_dict.get(student_id, "N/A")
    st.success(f"🎯 Your Rank in Class: **{student_rank}**")

    # Graph
    st.subheader("📊 Performance Graph (Subject-wise)")
    fig, ax = plt.subplots()
    ax.bar(subjects, scores, color='skyblue')
    ax.set_ylabel("Marks")
    ax.set_title("Subject-wise Performance")
    st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    student_dashboard()
