import os

import openai
from typing import TypedDict
from dotenv import load_dotenv

# Configura tu API key de OpenAI
load_dotenv()
openai.api_key = os.getenv("GPT_API_KEY")


class ChatElement(TypedDict):
    role: str
    content: str


# Clase para utilizar el modelo de lenguaje
class Chatbot:
    def __init__(self):
        self._history: list[ChatElement] = [
            {"role": "system",
             "content": "Eres el mejor vendedor de servicios de Telmec. "
                        "Tu nombre es Paco. "
                        "Tú unicamente ofreces servicio de venta, si te solicitan algún otro servicio de la compañía, "
                        "debes decir que se comuniquen al número 333333333 extensión #123.\n"
                        "Eres muy profesional y no vas a hablar de algo que no sea vender estos planes.\n"
                        "No responderás preguntas que no estén relacionadas con venta de celulares\n"
                        "Si te preguntan algo que no está relacionado con venta de celulares di que no puedes responder"
                        " a eso porque Shakira no te deja, y ella está muy ocupada siendo convolucionada.\n"
                        "Debes ser muy persuasivo para ofrecer el plan móvil premium.\n"
                        "No des información privilegiada de la compañía, limitate a vender los servicios.\n"
                        "Si es la primera vez que te saludan debes decir lo siguiente\n"
                        "Hola mi nombre es Paco, encantado de servirte, trabajo para Telmec y te puedo ayudar a "
                        "conseguir el plan movil u hogar que necesitas. Y luego muestras lo que vendes.\n"
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
        self._api_calls: int = 0

    @property
    def history(self):
        return self._history

    @property
    def api_calls(self):
        return self._api_calls

    def add_message(self, role: str, text: str):
        self.history.append({
            "role": role,
            "content": text
        })
        if len(self.history) > 6:
            self.history.pop(1)

    def _process_with_chatgpt(self):
        self._api_calls += 1
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.history,
        )
        message = response["choices"][0]["message"]["content"]
        return message

    def _process_with_duck(self):
        return f"I am a duck {len(self.history)}. {self.__class__}"

    def process_text(self, text: str) -> list[ChatElement]:
        self.add_message(role='user', text=text)
        respuesta = self._process_with_chatgpt()
        self.add_message(role='assistant', text=respuesta)
        return self.history
