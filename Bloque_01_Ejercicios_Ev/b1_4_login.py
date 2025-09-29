usuario_correcto = "admin"
contraseña_segura = "1234"
nombre = input("Nombre de usuario:")
contraseña = input("Contraseña:")

if (usuario_correcto == nombre ) and (contraseña == contraseña_segura):
    print("Acceso concedido")
else :
    print("Acceso denegado")
