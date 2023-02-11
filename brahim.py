from  PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="My Portfolio", page_icon=" :wave: ",layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
          return None
    return r.json()
#  Use Local CSS
def local_css(file_name):
      with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

local_css("styles\images\style.css")
# LOAD ASSETS
Lottie_coding = load_lottieurl ("https://assets9.lottiefiles.com/private_files/lf30_gcroxmlt.json")
img_First_form = Image.open("styles\images\First.png")
img_Second_form = Image.open("styles\images\Second.png")
img_Third_form = Image.open("styles\images\Third.png")
img_Fourth_form = Image.open("styles\images\Fourth.png")
# img_lottie_animation = Image.open("images/Screenshot 2023-02-06 165040.png")
# Header section
with st.container():
    st.subheader(" Hi! i'm Brahim Azzaf :wave:")
    st.title("Web development student From Morocco")
    st.write ("I'm passionate about programming npm install streamlit-component-lib")

         # WHAT I DO
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I'm learning development web using this following languages for front-end:

                - HTML
                - CSS  
                - JAVA SCRIPT
            And for the back-end:

                -PHP
                -PYTHON
                -DATA BASE
            """
                )
    with  right_column :
            st_lottie(Lottie_coding, height=500, key="lottie_coding")
        # ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    st.header("i already create my first template by ***HTML*** and ***CSS***")

image_column, text_column = st.columns((1, 3))
with image_column:
     st.image(img_First_form)
     
with text_column:
        st.subheader("this is some   pictures of my first try")
    # st.write("---")
    # st.header("My Projects")
        st.write("##")

# image_column, text_column = st.columns((1,3 ))
with image_column:
     st.image(img_Second_form)
with image_column:
          st.image(img_Third_form)

# ---- CONTACT ----
with st.container():
      st.write("---")
      st.header("Get In Touch With Me!")
      st.write("##")

# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
contact_form = """
    <form action="https://formsubmit.co/bazzaf21@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
    </form>
    """
left_column, right_column = st.columns(2)
with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
        st.empty()
