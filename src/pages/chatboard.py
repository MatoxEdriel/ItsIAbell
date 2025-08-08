import streamlit as st
from src.app.chatbot import get_response
import PyPDF2  
from streamlit_lottie import st_lottie



def run():
    st.title("💬 Consulta con LexIA")

    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = None

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


    prompt = st.chat_input("Escribe tu mensaje...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = get_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

    uploaded_file = st.file_uploader(
        "📄 Selecciona un archivo PDF para enviar",
        type=["pdf"],
        key="file_uploader"
    )
    
    if uploaded_file is not None:
        st.session_state.uploaded_file = uploaded_file

 
    if st.session_state.uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(st.session_state.uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"

   
        if "pdf_processed" not in st.session_state:
            response = get_response(text)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
               st.markdown(response)
            st.session_state.pdf_processed = True

