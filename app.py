import streamlit as st
s = "Salary Predictor"
st.set_page_config(page_title=s,page_icon="icon2.jpeg")

import base64
from predict import show_predict_page
from explore import show_explore_page

#background img/gif
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('SDE.gif')

page = st.sidebar.selectbox("Do You Want To Explore Or Predict ?", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

#To hide water mark

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#Feedbacks
with st.container():
    st.write("---")
    st.write("""## Get In Touch With Me For Feebacks/Suggestions !""")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/soulankit1234@gmail.com" method="POST">
        <input type="text" name = "name" placeholder = "Your name" required>
        <input type="email" name = "email" placeholder = "Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    <br>
    <body>
     <center><p>Made with ❤️ by Ankit Singh & Co. </p><center>
    </body>
    <center><a href="https://www.linkedin.com/in/ankit-singh-4b787a207">Connect With Me</a></center>
    <br>
    
    <body>
        <center><p>The Prediction May Not Be 100% Accurate</p><center>
    </body>
    """
    st.markdown(contact_form,unsafe_allow_html=True)