from config.settings import JARVIS_NAME, JARVIS_VERSION
from core.conversation import Conversation


class Jarvis:
    def __init__(self, provider):
        self.provider = provider
        self.name = JARVIS_NAME
        self.version = JARVIS_VERSION
        self.conversacion = Conversation()

    def procesar(self, mensaje):
        self.conversacion.agregar("usuario", mensaje)

        historial = self.conversacion.obtener_mensajes()
        respuesta = self.provider.responder(historial)

        self.conversacion.agregar("jarvis", respuesta)

        return respuesta