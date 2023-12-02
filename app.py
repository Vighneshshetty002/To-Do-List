# todo_app_with_visualizations.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Sample dataset
data = {
    'Task': ['Complete Project', 'Buy Groceries', 'Exercise', 'Read Book'],
    'Priority': ['High', 'Medium', 'Low', 'High'],
    'Due Date': ['2023-12-15', '2023-12-10', '2023-12-20', '2023-12-18'],
    'Description': ['Finish the Streamlit project', 'Get fruits and vegetables', 'Morning jog', 'Read "The Great Gatsby"']
}

df = pd.DataFrame(data)

# Streamlit App
st.title("To-Do List App with Dataset and Visualizations")

# Display the to-do list
st.subheader("To-Do List")
st.write(df)

# Visualizations
st.subheader("Task Priority Distribution - Pie Chart")
fig_pie = px.pie(df, names='Priority', title='Task Priority Distribution')
st.plotly_chart(fig_pie)

# Bar Graph for Task Priority Count
st.subheader("Task Priority Count - Bar Graph")
fig_bar = px.bar(df['Priority'].value_counts(), x=df['Priority'].value_counts().index, y=df['Priority'].value_counts().values, labels={'x': 'Priority', 'y': 'Count'}, title='Task Priority Count')
st.plotly_chart(fig_bar)

# Filter tasks based on priority
selected_priority = st.sidebar.selectbox("Filter by Priority", df['Priority'].unique())
filtered_df = df[df['Priority'] == selected_priority]

# Display filtered tasks
st.subheader(f"To-Do List (Priority: {selected_priority})")
st.write(filtered_df)

# Checkbox to mark tasks as completed
completed_task = st.checkbox("Mark as Completed")
if completed_task:
    st.success("Task marked as completed!")

# Button to clear completed tasks
if st.button("Clear Completed Tasks"):
    df = df[df['Task'].apply(lambda task: task not in st.multiselect("Completed Tasks", df['Task'].tolist()))]

# Button to clear all tasks
if st.button("Clear All Tasks"):
    df = pd.DataFrame(columns=['Task', 'Priority', 'Due Date', 'Description'])

# Display completed tasks
st.subheader("Completed Tasks")
st.write(df)