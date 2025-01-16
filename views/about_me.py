import streamlit as st

from form.contact import contact_form

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/profile.png", width=200)

with col2:
    st.title("Jyun-Yi Chen", anchor=False)
    st.write(
        "Research Assistant, designing A.I. systems to solve challenges in biomedicine."
    )
    if st.button("✉️ Contact Me"):
        contact_form()

st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
    - Bachelor of Electrical Engineering, National Taiwan Normal Univeristy (Graduated: 2022)
    - Master of Electrical Engineering, National Taiwan Normal Univeristy (Graduated: 2024)
    """
)

st.write("\n")
st.subheader("Skills", anchor=False)
st.write(
    """
    - Language: Chinese, English
    - Programming: Python, C++, Latex
    - Expertise: Machine Learning, Education Technology, Bioinformatics
    """
)