print("📓 Gestor de Notas")
archivo = "notas.txt"
modo = "r"
encoding = "utf-8"

# Aquí se comprueba si existe o no el archivo, para crearlo o mostrarlo
try:
    with open(archivo, modo, encoding=encoding) as f:
        print(f"Archivo encontrado: {archivo}")
        lineas = f.readlines()
        for i, lin in enumerate(lineas, start=1):
            print(f"{i}. {lin.strip()}")

except FileNotFoundError:
    # Si no existe, lo creamos vacío
    print("❌ El archivo no existe.")
    with open(archivo, "w", encoding=encoding) as f:
        f.write("") #Si no ponemos nada se creara vacío
except PermissionError:
    print("❌ No tienes permisos para acceder al archivo.")

# Esto es el bucle del programa
opcion = ""
while opcion != "4":
    print("\n=== MENU ===")
    print("1. Ver notas")
    print("2. Añadir nota")
    print("3. Eliminar nota")
    print("4. Salir")

    opcion = input("Elije una opción: ")

    match opcion:
        case "1":
            try:
                with open(archivo, "r", encoding=encoding) as f:
                    lineas = f.readlines()
                    for i, lin in enumerate(lineas, start=1):
                        print(f"{i}. {lin.strip()}")
            except FileNotFoundError:
                print("❌ El archivo no existe.")

        case "2":
            # Esto lo que hace es añadir una nota
            nueva_nota = input("Escribe la nueva nota: ")
            with open(archivo, "a", encoding=encoding) as f:
                f.write(f"{nueva_nota}\n")
                print("✅ Nota guardada con éxito.")

        case "3":
            try:
                # Primero esto lo que hace es leer todas las lineas
                with open(archivo, "r", encoding=encoding) as f:
                    lineas = f.readlines()

                # Aquí pide el número y lo valida
                num = int(input("Número de nota a eliminar: "))

                if 1 <= num <= len(lineas):
                    # 3. Eliminar y sobrescribir
                    lineas.pop(num - 1)
                    with open(archivo, "w", encoding=encoding) as f:
                        f.writelines(lineas)
                    print("✅ Nota eliminada.")
                else:
                    print("❌ El número no existe.")
            except ValueError:
                print("❌ Introduce un número, no letras.")

        case "4":
            print("👋 ¡Hasta la próxima!")
        case _:
            print("Opción invalida. Elije 1–4.")