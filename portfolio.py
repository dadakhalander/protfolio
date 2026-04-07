
import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="My Portfolio",
    page_icon="💼",
    layout="wide"
)

# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
st.sidebar.title("Portfolio Menu")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "About",
        "Skills",
        "Projects",
        "Experience",
        "Education",
        "Certificates",
        "Contact"
    ]
)

# -----------------------------
# HOME PAGE
# -----------------------------
if page == "Home":
    st.title("Your Name")
    st.subheader("Your Role / Profession")
    
    st.write("""
    Welcome to my portfolio website.
    
    Here you can learn more about me, my projects, skills, experience, and contact details.
    """)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("your_photo.jpg", width=250)

    with col2:
        st.write("Short introduction about yourself.")
        st.write("- Example: Python Developer")
        st.write("- Example: AI Enthusiast")
        st.write("- Example: Web Developer")

# -----------------------------
# ABOUT PAGE
# -----------------------------
elif page == "About":
    st.title("About Me")

    st.write("""
    Write a short summary about yourself here.

    Include:
    - Who you are
    - What you study or do
    - Your interests
    - Your goals
    """)

# -----------------------------
# SKILLS PAGE
# -----------------------------
elif page == "Skills":
    st.title("Skills")

    st.subheader("Technical Skills")
    st.write("""
    - Python
    - Streamlit
    - HTML / CSS
    - JavaScript
    - SQL
    - Machine Learning
    """)

    st.subheader("Soft Skills")
    st.write("""
    - Communication
    - Teamwork
    - Problem Solving
    - Time Management
    """)

# -----------------------------
# PROJECTS PAGE
# -----------------------------
elif page == "Projects":
    st.title("Projects")

    st.subheader("Project 1: Portfolio Website")
    st.write("""
    Description of your project.
    
    Technologies used:
    - Python
    - Streamlit
    """)

    st.link_button("View Project", "https://github.com/yourusername/project1")

    st.subheader("Project 2: Data Analysis Dashboard")
    st.write("""
    Description of another project.
    
    Technologies used:
    - Python
    - Pandas
    - Matplotlib
    """)

    st.link_button("View Project", "https://github.com/yourusername/project2")

# -----------------------------
# EXPERIENCE PAGE
# -----------------------------
elif page == "Experience":
    st.title("Experience")

    st.subheader("Job Title / Internship")
    st.write("""
    Company Name | Year
    
    - Responsibility 1
    - Responsibility 2
    - Responsibility 3
    """)

# -----------------------------
# EDUCATION PAGE
# -----------------------------
elif page == "Education":
    st.title("Education")

    st.subheader("University / College Name")
    st.write("""
    Degree Name
    
    Year: 2022 - 2026
    """)

# -----------------------------
# CERTIFICATES PAGE
# -----------------------------
elif page == "Certificates":
    st.title("Certificates")

    st.write("""
    - Python Certificate
    - Web Development Certificate
    - Data Science Certificate
    """)

# -----------------------------
# CONTACT PAGE
# -----------------------------
elif page == "Contact":
    st.title("Contact Me")

    st.write("Email: yourname@email.com")
    st.write("Phone: +123456789")
    st.write("LinkedIn: https://linkedin.com/in/yourprofile")
    st.write("GitHub: https://github.com/yourusername")

    st.subheader("Send a Message")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Submit"):
        st.success("Message sent successfully!")
