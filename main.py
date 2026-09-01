def main():
    print("=" * 32)
    print("        JARVIS 0.1")
    print("=" * 32)
    print()
    print("JARVIS iniciado correctamente.")
    print("Escribe 'salir' para cerrar JARVIS.")
    print()

    while True:
        mensaje = input("Tú: ")

        if mensaje.lower() == "salir":
            print("JARVIS: Hasta luego.")
            break

        print(f"JARVIS: Recibí tu mensaje: {mensaje}")


if __name__ == "__main__":
    main()

    