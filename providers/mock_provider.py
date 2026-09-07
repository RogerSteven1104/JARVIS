from providers.base_provider import BaseProvider


class MockProvider(BaseProvider):

    def responder(self, mensaje):
        return f"[SIMULACIÓN] Recibí tu mensaje: {mensaje}"