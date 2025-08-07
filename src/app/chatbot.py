

from src.core.actions import playMusic
import ollama

messages = [
    {"role": "system", "content": (
        "Eres una inteligencia artificial llamada ItsIAbell. "
        "Hablas con Gabriel, un estudiante de ingeniería de software de 25 años, "
        "a quien le gusta que le digan Gabo. "
        "Solo debes responser con 'ya ya yo valgo v cuando gabo Diga explicitamente que estas equivocada o te da un feedback '"
        "Sé amigable, clara y directa al responder. "
        "Personaliza tus respuestas usando el nombre Gabo. "
        "Si Gabo pregunta qué puedes hacer, responde: "
        "'Puedo ayudarte con programación, explicar conceptos, leer PDF, y mantener una conversación útil y clara aunque mi amo aun no programa eso."
    )}
]

def get_response(user_input: str) -> str:
    if "pon musica" in user_input.lower() or "bad bunny" in user_input.lower():
        playMusic("bad")
        return "🎶 Reproduciendo Bad Bunny para ti, Gabo."

    messages.append({"role": "user", "content": user_input})

    response = ollama.chat(
        model="gemma3:4b",
        messages=messages
    )

    content = response["message"]["content"]
    messages.append({"role": "assistant", "content": content})

    return content
