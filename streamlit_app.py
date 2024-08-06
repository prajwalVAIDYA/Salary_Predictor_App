import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go

# Load the pre-trained model
model = joblib.load('salary_pred_model.joblib')

dataset = pd.read_csv("Salary_Data_Based_country_and_race.csv")

# Function to predict salary
def predict_salary(age, gender, education_level, years_of_experience, job_title):
    # Prepare the input data for the model
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Education Level': [education_level],
        'Years of Experience': [years_of_experience],
        'Job Title': [job_title]
    })
    # Make prediction
    predicted_salary = model.predict(input_data)
    return predicted_salary[0]

# Streamlit app layout
st.title("Salary Prediction App")
st.sidebar.header("Input Parameters")

# Sidebar inputs
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.sidebar.selectbox("Gender", options=["Male", "Female", "Other"])
education_level = st.sidebar.selectbox("Education Level", options=["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
years_of_experience = st.sidebar.number_input("Years of Experience", min_value=0, max_value=50, value=5)

# Define the available job titles
job_titles = ['Software Engineer', 'Data Analyst', 'Senior Manager',
       'Sales Associate', 'Director', 'Marketing Analyst',
       'Product Manager', 'Sales Manager', 'Marketing Coordinator',
       'Senior Scientist', 'Software Developer', 'HR Manager',
       'Financial Analyst', 'Project Manager', 'Customer Service Rep',
       'Operations Manager', 'Marketing Manager', 'Senior Engineer',
       'Data Entry Clerk', 'Sales Director', 'Business Analyst',
       'VP of Operations', 'IT Support', 'Recruiter', 'Financial Manager',
       'Social Media Specialist', 'Software Manager', 'Junior Developer',
       'Senior Consultant', 'Product Designer', 'CEO', 'Accountant',
       'Data Scientist', 'Marketing Specialist', 'Technical Writer',
       'HR Generalist', 'Project Engineer', 'Customer Success Rep',
       'Sales Executive', 'UX Designer', 'Operations Director',
       'Network Engineer', 'Administrative Assistant',
       'Strategy Consultant', 'Copywriter', 'Account Manager',
       'Director of Marketing', 'Help Desk Analyst',
       'Customer Service Manager', 'Business Intelligence Analyst',
       'Event Coordinator', 'VP of Finance', 'Graphic Designer',
       'UX Researcher', 'Social Media Manager', 'Director of Operations',
       'Senior Data Scientist', 'Junior Accountant',
       'Digital Marketing Manager', 'IT Manager',
       'Customer Service Representative', 'Business Development Manager',
       'Senior Financial Analyst', 'Web Developer', 'Research Director',
       'Technical Support Specialist', 'Creative Director',
       'Senior Software Engineer', 'Human Resources Director',
       'Content Marketing Manager', 'Technical Recruiter',
       'Sales Representative', 'Chief Technology Officer',
       'Junior Designer', 'Financial Advisor', 'Junior Account Manager',
       'Senior Project Manager', 'Principal Scientist',
       'Supply Chain Manager', 'Senior Marketing Manager',
       'Training Specialist', 'Research Scientist',
       'Junior Software Developer', 'Public Relations Manager',
       'Operations Analyst', 'Product Marketing Manager',
       'Senior HR Manager', 'Junior Web Developer',
       'Senior Project Coordinator', 'Chief Data Officer',
       'Digital Content Producer', 'IT Support Specialist',
       'Senior Marketing Analyst', 'Customer Success Manager',
       'Senior Graphic Designer', 'Software Project Manager',
       'Supply Chain Analyst', 'Senior Business Analyst',
       'Junior Marketing Analyst', 'Office Manager', 'Principal Engineer',
       'Junior HR Generalist', 'Senior Product Manager',
       'Junior Operations Analyst', 'Senior HR Generalist',
       'Sales Operations Manager', 'Senior Software Developer',
       'Junior Web Designer', 'Senior Training Specialist',
       'Senior Research Scientist', 'Junior Sales Representative',
       'Junior Marketing Manager', 'Junior Data Analyst',
       'Senior Product Marketing Manager', 'Junior Business Analyst',
       'Senior Sales Manager', 'Junior Marketing Specialist',
       'Junior Project Manager', 'Senior Accountant', 'Director of Sales',
       'Junior Recruiter', 'Senior Business Development Manager',
       'Senior Product Designer', 'Junior Customer Support Specialist',
       'Senior IT Support Specialist', 'Junior Financial Analyst',
       'Senior Operations Manager', 'Director of Human Resources',
       'Junior Software Engineer', 'Senior Sales Representative',
       'Director of Product Management', 'Junior Copywriter',
       'Senior Marketing Coordinator', 'Senior Human Resources Manager',
       'Junior Business Development Associate', 'Senior Account Manager',
       'Senior Researcher', 'Junior HR Coordinator',
       'Director of Finance', 'Junior Marketing Coordinator',
       'Junior Data Scientist', 'Senior Operations Analyst',
       'Senior Human Resources Coordinator', 'Senior UX Designer',
       'Junior Product Manager', 'Senior Marketing Specialist',
       'Senior IT Project Manager', 'Senior Quality Assurance Analyst',
       'Director of Sales and Marketing', 'Senior Account Executive',
       'Director of Business Development', 'Junior Social Media Manager',
       'Senior Human Resources Specialist', 'Senior Data Analyst',
       'Director of Human Capital', 'Junior Advertising Coordinator',
       'Junior UX Designer', 'Senior Marketing Director',
       'Senior IT Consultant', 'Senior Financial Advisor',
       'Junior Business Operations Analyst',
       'Junior Social Media Specialist',
       'Senior Product Development Manager', 'Junior Operations Manager',
       'Senior Software Architect', 'Junior Research Scientist',
       'Senior Financial Manager', 'Senior HR Specialist',
       'Senior Data Engineer', 'Junior Operations Coordinator',
       'Director of HR', 'Senior Operations Coordinator',
       'Junior Financial Advisor', 'Director of Engineering',
       'Software Engineer Manager', 'Back end Developer',
       'Senior Project Engineer', 'Full Stack Engineer',
       'Front end Developer', 'Front End Developer',
       'Director of Data Science', 'Human Resources Coordinator',
       'Junior Sales Associate', 'Human Resources Manager',
       'Juniour HR Generalist', 'Juniour HR Coordinator',
       'Digital Marketing Specialist', 'Receptionist',
       'Marketing Director', 'Social Media Man', 'Delivery Driver']

# Search for job titles and combine with job title selection
search_term = st.sidebar.text_input("Search Job Titles", "")
filtered_job_titles = [title for title in job_titles if search_term.lower() in title.lower()]

# If no titles match, show a message
if not filtered_job_titles:
    filtered_job_titles = ["No matching job titles"]

# Create the selectbox with the filtered options
job_title = st.sidebar.selectbox("Job Title", options=filtered_job_titles)

# Validation for years of experience
if years_of_experience >= age - 18:
    st.sidebar.error("Years of Experience must be at least 18 years less than Age.")
else:
    # Predict salary when inputs are valid
    if st.sidebar.button("Predict Salary"):
        salary = predict_salary(age, gender, education_level, years_of_experience, job_title)
      # Enhanced Visualization
        st.success(f"The predicted salary for the position of **{job_title}** is: **${salary:,.2f}**")

        # Create a Plotly bar chart to visualize the predicted salary
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=[job_title],
            y=[salary],
            marker_color='skyblue'
        ))

        # Update layout for better appearance
        fig.update_layout(
            title='Predicted Salary',
            xaxis_title='Job Title',
            yaxis_title='Salary ($)',
            yaxis=dict(range=[0, salary * 1.2]),  # Extend y-axis limits for better visualization
            template='plotly_white'
        )

        # Display the Plotly figure
        st.plotly_chart(fig)
        # Create a Plotly box plot to visualize the salary trends
        fig = go.Figure()
        fig.add_trace(go.Box(
            y=dataset['Salary'],
            x=dataset['Country'],
            marker_color='skyblue'
        ))

        # Update layout for better appearance
        fig.update_layout(
            title=f'Salary Trends for {job_title}',
            xaxis_title='Country',
            yaxis_title='Salary ($)',
            template='plotly_white'
        )

        # Display the Plotly figure
        st.plotly_chart(fig)
