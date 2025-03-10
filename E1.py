# Stack

texto = []
agregar_texto = input("\nIngrese texto a la pila de texto\n")
texto.append(agregar_texto)
agregar_texto = input("\nIngrese texto a la pila de texto\n")
texto.append(agregar_texto)
agregar_texto = input("\nIngrese texto a la pila de texto\n")
texto.append(agregar_texto)
agregar_texto = input("\nIngrese texto a la pila de texto\n")
texto.append(agregar_texto)

print(texto)

eliminar_texto = input("\nElimine el ultimo texto que ingreso\n")
texto.pop(eliminar_texto)

print(f"Se elimino corectamente {texto.pop()}")
informacion = texto.peek()


# Stack

texto = []

for _ in range(4):  # Permite ingresar 4 textos sin repetir código
    agregar_texto = input("\nIngrese texto a la pila de texto: ")
    texto.append(agregar_texto)

print("\nContenido de la pila:", texto)

input("\nPresione Enter para eliminar el último texto...\n")
eliminado = texto.pop()
print(f"\nSe eliminó correctamente: {eliminado}")

if texto:  # Verifica que la pila no esté vacía antes de acceder
    ultimo = texto[-1]
    print(f"\nÚltimo texto en la pila: {ultimo}")
else:
    print("\nLa pila está vacía.")
