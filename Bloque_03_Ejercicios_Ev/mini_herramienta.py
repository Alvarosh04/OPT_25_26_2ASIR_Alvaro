opcion = ""
while opcion != "4":
    print("\n=== MENU ===")
    print("1. Calculos matematicos")
    print("2. Explorador de directorios")
    print("3. Consulta API (request)")
    print("4. Salir")

    opcion = input("Elije una opción: ")

    match opcion:
        case "1":
            try:
                num = int(input("Escribe un número: "))
                import math
                print("Raíz cuadrada:", math.sqrt(num))
                print("Factorial:", math.factorial(num))
                print("Potencia al cuadrado: ", math.pow(num,2))
            except ValueError:
                print("❌ Error: Debes introducir un número válido.")
            except OverflowError:
                print("❌ Error: El número es demasiado grande para calcular su factorial.")

        case "2":
            import os
            print("Directorio actual:", os.getcwd())
            print("Archivos en la carpeta:")
            for nombre in os.listdir("."):
                print("-", nombre)
            nueva_carp = input("¿Quieres crear una nueva carpeta? (s/n)")
            if nueva_carp == "s":
                nom_carp = input("Introduce el nombre de la carpeta")
                try:
                    os.mkdir(nom_carp)
                    print("✅ Carpeta creada con éxito.")
                except FileExistsError:
                    print("❌ Error: La carpeta ya existe.")

        case "3":
            import requests
            url = "https://api.github.com"
            print(f"Peticion a: {url}")
            resp = requests.get(url)
            print(f"Código de estado: {resp.status_code}")
            print(f"Tamaño de la respuesta: {len(resp.text)} caracteres")
            print("Contenido (200 caracteres):")
            print(resp.text[:200])

        case "4":
            print("👋¡Hasta la próxima!")

        case _:
            print("Opción no valida")