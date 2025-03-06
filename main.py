import streamlit as st
from PIL import Image

# Sidebar Navigation with Icons
st.sidebar.title("📌Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "📂 Projects", "💪 Skills", "💬 Testimonials", "📞 Contact"]
)

# Home Section
if page == "🏠 Home":
    image = Image.open("img.jpg")  # Ensure your image filename is correct
    st.image(image, caption="CIMANUKA B.M", width=200)
    st.title("My Digital Footprint")
    st.write("### Welcome to My Portfolio")
    st.write("I am passionate about technology and software development, with hands-on experience in building projects and solving real-world problems.")
    

# Projects Section
elif page == "📂 Projects":
    st.header("Projects")
    st.write("### 1. Student Career Guidance System")
    st.write("Individual Project using Python")
    st.write("[GitHub Link](https://github.com/Mona0009/student-career-guidance)")
    st.write("[LinkedIn](https://www.linkedin.com/in/exaucia-kim-9b996029a/e)")

    st.write("### 2. Malaria Diagnosis System")
    st.write("Group Project using Python")
    st.write("[GitHub Link](https://github.com/Mona0009/malaria-diagnosis-system)")

# Skills Section
elif page == "💪 Skills":
    st.header("Skills")
    st.write("#### Programming Languages")
    st.progress(80)
    st.write("Python - 80%")
    st.progress(70)
    st.write("Machine Learning - 70%")
    st.progress(60)
    st.write("Web Development - 60%")

# Testimonials Section
elif page == "💬 Testimonials":
    st.header("Testimonials")
    st.write("> CIMANUKA B.M is a brilliant problem solver! – Mima Z.C ❤")
    st.write("> CIMANUKA B.M's projects are innovative – Akazaah 😈")
    st.write("> CIMANUKA B.M is a chill guy – Nono ❤")

# Contact Section
elif page == "📞 Contact":
    st.header("Contact")
    st.write("Feel free to reach out via my LinkedIn or GitHub profiles!")
    st.write("[LinkedIn](https://www.linkedin.com/in/exaucia-kim-9b996029a/e)")
    st.write("[GitHub](https://github.com/Mona0009)")
    # Resume Download Button
with open("CIMANUKA_CV.pdf", "rb") as file:
    st.sidebar.download_button("Download CIMANUKA_CV", file, file_name="CIMANUKA_CV.pdf")