class Jarvis:
    def __init__(self, provider):
        self.provider = provider

    def procesar(self, mensaje):
        return self.provider.responder(mensaje)
