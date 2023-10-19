import streamlit as st

from interfaz import Chatbot
from interfaz import ChatElement
from itertools import islice


def show_chat_history(messages: list[ChatElement]):
    history = ""
    for message in messages:
        role = message["role"]
        content = message["content"]
        history += f"{role}: {content}\n"
    return history


# Función principal para la aplicación de Streamlit
def main(chatbot: Chatbot):
    st.title("Chatbot con GPT-3.5 Turbo")

    user_input = st.text_input("Tú:", "")

    if user_input:
        response = chatbot.process_text(user_input)
        reversed_response = list(islice(reversed(response[1:]), 5))
        history = show_chat_history(reversed_response)
        st.text_area("Historial de chat", value=history, height=400)


if __name__ == "__main__":
    if 'chatbot' not in st.session_state:
        st.session_state['chatbot'] = Chatbot()

    main(st.session_state['chatbot'])
