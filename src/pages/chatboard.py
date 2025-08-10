import streamlit as st
import camelot
import tempfile
import os
from google.cloud import aiplatform

# Configuración del proyecto
PROJECT_ID = "innate-watch-468517-v9"
LOCATION = "us-central1"
ENDPOINT_ID = "2170597581439107072"

# Ruta absoluta al archivo JSON con credenciales
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Gabriel Campoverde\Desktop\NovaCode\ItsIAbell\innate-watch-468517-v9-5e19a278f28d.json"

# Inicializa el cliente de Vertex AI
aiplatform.init(project=PROJECT_ID, location=LOCATION)

def get_response(messages) -> str:
    """
    Envía la lista completa de mensajes al endpoint de Vertex AI y devuelve la respuesta.
    messages: lista de dicts con "role" y "content".
    """
    try:
        endpoint = aiplatform.Endpoint(
            endpoint_name=f"projects/{PROJECT_ID}/locations/{LOCATION}/endpoints/{ENDPOINT_ID}"
        )

        response = endpoint.predict(
            instances=[
                {
                    "messages": messages
                }
            ],
            parameters={
                "temperature": 0.5,
                "maxTokens": 1000,
                "topP": 0.95,
                "topK": 40,
            }
        )

        if response.predictions:
            pred = response.predictions[0]
            if isinstance(pred, dict):
                return pred.get("content") or pred.get("text") or str(pred)
            else:
                return str(pred)
        else:
            return "No se obtuvieron predicciones."

    except Exception as e:
        return f"Error en la llamada a Vertex AI: {e}"

def run():
    st.title("💬 Consulta con LexIA (Extracción con Camelot y Vertex AI)")

    if "messages" not in st.session_state:
        # Mensaje sistema inicial para dar contexto al asistente
        st.session_state.messages = [
            {"role": "system", "content": "Eres un asistente conversacional útil y amigable."}
        ]
    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = None
    if "pdf_processed" not in st.session_state:
        st.session_state.pdf_processed = False

    # Mostrar mensajes previos (excepto system)
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    prompt = st.chat_input("Escribe tu mensaje...")
    if prompt:
        # Añadir mensaje usuario a la conversación
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Enviar toda la conversación para obtener respuesta contextual
        response = get_response(st.session_state.messages)
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
        st.session_state.pdf_processed = False  # Reset para nuevo archivo

    if st.session_state.uploaded_file is not None and not st.session_state.pdf_processed:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(st.session_state.uploaded_file.read())
            tmp_file_path = tmp_file.name

        try:
            tables = camelot.read_pdf(tmp_file_path, pages='1-end', flavor='stream')
            st.write(f"Se encontraron {tables.n} tablas en el PDF.")

            all_tables_text = ""
            for i, table in enumerate(tables):
                st.write(f"Tabla {i+1}")
                st.dataframe(table.df)
                all_tables_text += table.df.to_csv(index=False) + "\n\n"

            if all_tables_text.strip() == "":
                st.warning("No se pudo extraer texto de las tablas del PDF.")
            else:
                prompt_tablas = (
                    "Aquí tienes datos extraídos de tablas en formato CSV:\n\n"
                    + all_tables_text
                    + "\n\nPor favor, realiza un análisis breve y claro de estos datos."
                )
                # Añadir texto de las tablas como mensaje user para contexto
                st.session_state.messages.append({"role": "user", "content": prompt_tablas})

                response = get_response(st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": response})
                with st.chat_message("assistant"):
                    st.markdown(response)

            st.session_state.pdf_processed = True

        except Exception as e:
            st.error(f"Error procesando el PDF con Camelot: {e}")

if __name__ == "__main__":
    run()
