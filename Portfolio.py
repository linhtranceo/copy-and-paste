import streamlit as st
import info
import pandas as pd

#About me
def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width=200)
    st.write(info.about_me)
    st.write('---')
about_me_section()

#Sidebar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link=f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(github_link,unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html=f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt = "Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html,unsafe_allow_html=True)
links_section()

#Education
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework=pd.DataFrame(course_data)
    st.dataframe(coursework,column_config={
        "code": "Course Code",
        "names":"Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True,
        )
    st.write("--")
    
    

education_section(info.education_data, info.course_data)

#Professional Experience

def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title,(job_description, image) in experience_data.item():
        expnder = st.expander(f"{job_title}")
        expander:image(image,width=250)
        for bullet in job_description:
            expander:write(bullet)
    st.write("--")
experience_section(info_experience_data)






        
        
    
    
    
    

    
    
