from core.jarvis import Jarvis
from providers.mock_provider import MockProvider


def main():
    print("=" * 32)
    print("        JARVIS 0.1")
    print("=" * 32)
    print()
    print("JARVIS iniciado correctamente.")
    print("Escribe 'salir' para cerrar JARVIS.")
    print()

    provider = MockProvider()
    jarvis = Jarvis(provider)

    while True:
        mensaje = input("Tú: ")

        if mensaje.lower() == "salir":
            print("JARVIS: Hasta luego.")
            break

        respuesta = jarvis.procesar(mensaje)
        print(f"JARVIS: {respuesta}")

    print(jarvis.conversacion.obtener_mensajes())

if __name__ == "__main__":
    main()
