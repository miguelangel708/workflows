import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde lenguajes!")


if __name__ == "__main__":
    main()