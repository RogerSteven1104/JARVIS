from providers.base_provider import BaseProvider


class MockProvider(BaseProvider):

    def responder(self, historial):
        ultimo_mensaje = historial[-1]["contenido"]

        return f"[SIMULACIÓN] Recibí tu mensaje: {ultimo_mensaje}"