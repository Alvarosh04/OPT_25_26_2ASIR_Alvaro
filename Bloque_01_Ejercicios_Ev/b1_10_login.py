"""
Este programa simula el funcionamiento básico de un sistema de registro e inicio de sesión.
Permite a los usuarios registrarse con un correo electrónico y una contraseña segura, validando
ambos campos según las reglas indicadas. Incluye control de intentos fallidos e interfaz amigable.

"""

import re


def validar_identificador(identificador):
    """
    Valida que el identificador (email) cumpla con las reglas:
    - Mínimo 3 caracteres.
    - Contenga '@'.
    - Contenga alguna extensión válida (.com, .es, .net).
    - No contenga símbolos especiales (!#$%&*?).
    """
    if len(identificador) < 3:
        print(" El identificador debe tener al menos 3 caracteres.")
        return False

    if '@' not in identificador:
        print(" El identificador debe contener '@'.")
        return False

    if not (identificador.endswith(".com") or identificador.endswith(".es") or identificador.endswith(".net")):
        print(" El identificador debe terminar en .com, .es o .net.")
        return False

    if re.search(r"[!#$%&*?]", identificador):
        print(" El identificador no debe contener símbolos especiales (!#$%&*?).")
        return False

    return True


def validar_contraseña(contraseña):
    """
    Valida que la contraseña cumpla con las reglas:
    - Mínimo 8 caracteres.
    - Al menos una mayúscula.
    - Al menos un número.
    - Al menos un símbolo especial (!@#$%&*?).
    """
    if len(contraseña) < 8:
        print(" La contraseña debe tener al menos 8 caracteres.")
        return False
    if not re.search(r"[A-Z]", contraseña):
        print(" La contraseña debe contener al menos una letra mayúscula.")
        return False
    if not re.search(r"\d", contraseña):
        print(" La contraseña debe contener al menos un número.")
        return False
    if not re.search(r"[!@#$%&*?]", contraseña):
        print(" La contraseña debe contener al menos un símbolo especial (!@#$%&*?).")
        return False
    return True


def registrar_usuario():
    """
    Permite registrar un nuevo usuario validando identificador y contraseña.
    Devuelve el identificador y contraseña registrados.
    """
    print("\n---  Registro de nuevo usuario ---")

    while True:
        identificador = input("Ingrese su identificador (correo electrónico): ").strip()
        if validar_identificador(identificador):
            break

    while True:
        contraseña = input("Cree una contraseña segura: ")
        if validar_contraseña(contraseña):
            break

    print("✅ Usuario registrado con éxito.")
    return identificador, contraseña


def iniciar_sesion(identificador_guardado, contraseña_guardada):
    """
    Permite iniciar sesión verificando identificador y contraseña.
    Tiene un máximo de 3 intentos antes de regresar al menú.
    """
    print("\n---  Inicio de sesión ---")
    identificador = input("Identificador (correo electrónico): ").strip()

    if identificador != identificador_guardado:
        print(" Acceso denegado. El usuario no existe.")
        return

    intentos = 3
    while intentos > 0:
        contraseña = input("Contraseña: ")
        if contraseña == contraseña_guardada:
            print(" Acceso concedido.")
            return
        else:
            intentos -= 1
            print(f" Contraseña incorrecta. Intentos restantes: {intentos}")

    print(" Demasiados intentos fallidos. Regresando al menú principal.")


def menu_principal():
    """
    Muestra el menú principal y controla la navegación del programa.
    """
    identificador = None
    contraseña = None

    while True:
        print("\n===  MENÚ PRINCIPAL ===")
        print("[1] Registrarse")
        print("[2] Iniciar sesión")
        print("[3] Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            identificador, contraseña = registrar_usuario()
        elif opcion == "2":
            if identificador is None:
                print(" No hay usuarios registrados. Regístrese primero.")
            else:
                iniciar_sesion(identificador, contraseña)
        elif opcion == "3":
            print(" Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("️ Opción no válida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()
