import streamlit as st
from streamlit_lottie import st_lottie
import json
from src.pages import dashboard
from src.pages import chatboard
from src.app.animation import welcomeGabriel

def load_lottiefile(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def main():

    lottie_logo = load_lottiefile("src/assets/lottie/logo.json")

   
    with st.sidebar:
        st_lottie(lottie_logo, height=120)
        st.title("LexIA")
        page = st.radio("Select your Agent", ["Chatboard"])
    
   
    if page == "Chatboard":
        chatboard.run()
   

  
    welcomeGabriel()

if __name__ == "__main__":
    main()
