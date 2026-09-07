from config.settings import JARVIS_NAME, JARVIS_VERSION


class Jarvis:
    def __init__(self, provider):
        self.provider = provider
        self.name = JARVIS_NAME
        self.version = JARVIS_VERSION

    def procesar(self, mensaje):
        return self.provider.responder(mensaje)