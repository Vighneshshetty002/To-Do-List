# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load or initialize the dataset
data = {
    'Task': ['Complete Project', 'Buy Groceries', 'Exercise', 'Read Book'],
    'Priority': ['High', 'Medium', 'Low', 'High'],
    'Due Date': ['2023-12-15', '2023-12-10', '2023-12-20', '2023-12-18'],
    'Description': ['Finish the Streamlit project', 'Get fruits and vegetables', 'Morning jog', 'Read "The Great Gatsby"']
}

df = pd.DataFrame(data)

# Streamlit App
st.title("🚀 To-Do List App with Dataset and Visualizations 📊")
st.subheader("Your Personal Productivity Assistant")

# New Task Input Section
st.subheader("Add New Task")

# Input fields for new task
new_task = st.text_input("Task", "")
new_priority = st.selectbox("Priority", ['High', 'Medium', 'Low'])
new_due_date = st.date_input("Due Date")
new_description = st.text_area("Description", "")

# Button to add new task
if st.button("Add Task"):
    if new_task and new_due_date:
        new_task_data = {'Task': [new_task],
                         'Priority': [new_priority],
                         'Due Date': [str(new_due_date)],
                         'Description': [new_description]}

        # Append new task data to the existing DataFrame
        df = pd.concat([df, pd.DataFrame(new_task_data)], ignore_index=True)
        st.success("Task added successfully!")

        # Display the success message or any other relevant information
        st.subheader("Updated To-Do List")
        st.write("Task added successfully!")
    else:
        st.warning("Task name and due date are required to add a new task.")

# Visualizations
# (Keep the visualization and other sections the same as before)
