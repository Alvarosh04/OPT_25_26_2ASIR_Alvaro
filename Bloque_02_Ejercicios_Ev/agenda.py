agenda = {}

nom1 = input("Introduzca el nombre")
telf1 = input("Introduzca el  telefono")
nom2 = input("Introduzca el nombre")
telf2 = input("Introduzca el  telefono")
nom3 = input("Introduzca el nombre")
telf3 = input("Introduzca el  telefono")

agenda[nom1] = telf1
agenda[nom2] = telf2
agenda[nom3] =telf3

print("Agenda completa:")
for nombre, telefono in agenda.items():
    print(nombre, ":", telefono)

contacto = input("Intoduce un nombre, para buscar contacto")
if contacto in agenda:
    print(f"telefono: {agenda[contacto]}")
else:
    print("Usuario no encontrado")