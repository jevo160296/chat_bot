import streamlit as st

from interfaz import Chatbot
from interfaz import ChatElement
from itertools import islice


def show_chat_history(messages: list[ChatElement]):
    history = ""
    for message in messages:
        role = message["role"]
        content = message["content"]
        history += f"{role}: {content}\n\n"
    return history


# Función principal para la aplicación de Streamlit
def main(chatbot: Chatbot):
    st.title("Chatbot con GPT-3.5 Turbo.")

    if 'user_input' not in st.session_state:
        st.session_state.user_input = ''

    def submit():
        st.session_state.user_input = st.session_state.widget
        st.session_state.widget = ''

    st.text_input('Tú:', key='widget', on_change=submit)

    user_input = st.session_state.user_input

    if user_input:
        response = chatbot.process_text(user_input)
        reversed_response = list(islice(reversed(response[1:]), 5))
        history = show_chat_history(reversed_response)
        st.text_area("Historial de chat", value=history, height=400)

    st.subheader(f"API calls: {chatbot.api_calls}")


if __name__ == "__main__":
    if 'chatbot' not in st.session_state:
        st.session_state['chatbot'] = Chatbot()

    main(st.session_state['chatbot'])
