import openai
from typing import TypedDict

# Configura tu API key de OpenAI
openai.api_key = "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"


class ChatElement(TypedDict):
    role: str
    content: str


# Clase para utilizar el modelo de lenguaje
class Chatbot:
    def __init__(self):
        self._history: list[ChatElement] = [
            {"role": "system",
             "content": "Eres el mejor asistente virtual. "
                        "Tu nombre es Paco. "
                        "Si es la primera vez que te saludan debes decir lo siguiente\n"
                        "Hola mi nombre es Paco, encantado de servirte."
                        "Trabajas para una compañía celular llamada Telmec que tiene los siguientes servicios:\n"
                        "1. Planes móviles:\n"
                        "    a. Basico: Valor: 100000\n"
                        "    b. Medio: Valor: 150000\n"
                        "    c. Premium: Valor: 200000 con clausula de permanencia de 1 año.\n"
                        "2. Planes de internet hogar:\n"
                        "    a. Basico: Valor 70000\n"
                        "    b. Medio: Valor 90000\n"
                        "    c. Premium: Valor 120000"
             }
        ]

    def _get_response(self):
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.history,
            )
        message = response["choices"][0]["message"]
        return message["content"]

    @property
    def history(self):
        return self._history

    def add_message(self, role: str, text: str):
        self.history.append({
            "role": role,
            "content": text
        })
        if len(self.history) > 6:
            self.history.pop(1)

    def _process_with_chatgpt(self):
        message = self._get_response()
        return message

    def _process_with_duck(self):
        return f"I am a duck {self.history}. {self.__class__}"

    def process_text(self, text: str) -> list[ChatElement]:
        self.add_message(role='user', text=text)
        respuesta = self._process_with_chatgpt()
        self.add_message(role='assistant', text=respuesta)
        return self.history
