# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load or initialize the dataset
data = {
    'Task': ['Complete Project', 'Buy Groceries', 'Exercise', 'Read Book'],
    'Priority': ['High', 'Medium', 'Low', 'High'],
    'Due Date': ['2023-12-15', '2023-12-10', '2023-12-20', '2023-12-18'],
    'Description': ['Finish the Streamlit project', 'Get fruits and vegetables', 'Morning jog', 'Read "The Great Gatsby"'],
    'Completed': [False, False, False, False]
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
                         'Description': [new_description],
                         'Completed': [False]}

        # Append new task data to the existing DataFrame
        df = pd.concat([df, pd.DataFrame(new_task_data)], ignore_index=True)
        st.success("Task added successfully!")

        # Display the updated to-do list
        st.subheader("Updated To-Do List")
        st.write(df)

        # Display visualizations
        st.sidebar.subheader("Task Priority Distribution - Pie Chart")
        fig_pie = px.pie(df, names='Priority', title='Task Priority Distribution')
        st.sidebar.plotly_chart(fig_pie)

        st.sidebar.subheader("Task Priority Count - Bar Graph")
        fig_bar = px.bar(df['Priority'].value_counts().sort_index(), x=df['Priority'].value_counts().sort_index().index, y=df['Priority'].value_counts().sort_index().values, labels={'x': 'Priority', 'y': 'Count'}, title='Task Priority Count')
        st.sidebar.plotly_chart(fig_bar)

# Filter and Search Section
st.subheader("Filter and Search")

# Filter tasks by completion status
completed_filter = st.checkbox("Show Completed Tasks")
filtered_df = df[df['Completed'] == True] if completed_filter else df[df['Completed'] == False]

# Display filtered tasks
st.subheader("Filtered To-Do List")
st.write(filtered_df)

# Search tasks
search_term = st.text_input("Search Tasks")
if search_term:
    search_result = df[df['Task'].str.contains(search_term, case=False, na=False)]
    st.subheader(f"Search Results for '{search_term}'")
    st.write(search_result)

# Task Statistics
st.subheader("Task Statistics")
task_stats = pd.DataFrame({
    'Total Tasks': [len(df)],
    'Completed Tasks': [len(df[df['Completed']])],
    'Incomplete Tasks': [len(df[df['Completed'] == False])],
})

st.write(task_stats)

# Export to CSV
if st.button("Export To-Do List to CSV"):
    df.to_csv("to_do_list.csv", index=False)
    st.success("To-Do List exported to 'to_do_list.csv'")
