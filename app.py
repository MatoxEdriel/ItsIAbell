from src.app.animation import welcomeGabriel
from PIL import Image
import streamlit as st
import os
from src.pages import dashboard
from src.pages import chatboard

logo_path = os.path.join("src", "assets", "spider.jpeg")
logo = Image.open(logo_path)
st.sidebar.image(logo, width=120)

st.sidebar.title("ItsIAbell")

page = st.sidebar.radio("Select your Agent", ["Dashboard", "Chatboard"])

if page == "Dashboard":
    dashboard.run()

elif page == "Chatboard":
    chatboard.run()

welcomeGabriel()
