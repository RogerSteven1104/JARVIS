from core.conversation import Conversation


def test_agregar_mensaje():
    conversacion = Conversation()

    conversacion.agregar("usuario", "Hola JARVIS")

    mensajes = conversacion.obtener_mensajes()

    assert len(mensajes) == 1
    assert mensajes[0]["rol"] == "usuario"
    assert mensajes[0]["contenido"] == "Hola JARVIS"