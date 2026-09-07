class Conversation:
    def __init__(self):
        self.mensajes = []

    def agregar(self, rol, contenido):
        self.mensajes.append({
            "rol": rol,
            "contenido": contenido
        })

    def obtener_mensajes(self):
        return self.mensajes
