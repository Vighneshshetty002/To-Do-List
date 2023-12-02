# todo_app_with_dataset.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Sample dataset
data = {
    'Task': ['Complete Project', 'Buy Groceries', 'Exercise', 'Read Book', 'Write Blog Post', 'Attend Meeting', 'Prepare Presentation'],
    'Priority': ['High', 'Medium', 'Low', 'High', 'Medium', 'High', 'Medium'],
    'Due Date': ['2023-12-15', '2023-12-10', '2023-12-20', '2023-12-18', '2023-12-22', '2023-12-14', '2023-12-17'],
    'Description': ['Finish the Streamlit project', 'Get fruits and vegetables', 'Morning jog', 'Read "The Great Gatsby"',
                    'Write about Streamlit usage', 'Discuss project updates', 'Prepare slides for the meeting']
}

df = pd.DataFrame(data)

# Streamlit App
st.title("To-Do List App with Dataset")

# Display the to-do list
st.subheader("To-Do List")
st.write(df)

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

# Line Chart
st.subheader("Line Chart")
fig_line = px.line(df, x='Task', y='Due Date', title='Due Dates for Tasks')
st.plotly_chart(fig_line)

# Bar Chart
st.subheader("Bar Chart")
fig_bar = px.bar(df, x='Task', y='Due Date', title='Due Dates for Tasks')
st.plotly_chart(fig_bar)

# Histogram
st.subheader("Histogram")
fig_hist = px.histogram(df, x='Priority', title='Priority Distribution')
st.plotly_chart(fig_hist)

# Scatter Plot
st.subheader("Scatter Plot")
fig_scatter = px.scatter(df, x='Priority', y='Due Date', color='Priority', title='Scatter Plot')
st.plotly_chart(fig_scatter)

# Box Plot
st.subheader("Box Plot")
fig_box = px.box(df, x='Priority', y='Due Date', color='Priority', title='Box Plot')
st.plotly_chart(fig_box)
