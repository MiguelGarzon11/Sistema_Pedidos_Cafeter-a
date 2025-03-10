# Stack - Undo & Redo

pila = []
pila_redo = []

# Agregar textos a la pila
for _ in range(3):
    agregar_pila = input("\nIngrese un texto: ")
    pila.append(agregar_pila)

print("\nPila actual:", pila)

# Bucle para repetir acciones de deshacer y rehacer
while True:
    opcion = input("\nDigite (1) para deshacer, (2) para rehacer, (3) para salir: ").strip()

    if opcion == "1":  # Deshacer
        if pila:
            texto_eliminado = pila.pop()
            pila_redo.append(texto_eliminado)
            print("\nSe eliminó:", texto_eliminado)
        else:
            print("\nNo hay elementos para deshacer.")

    elif opcion == "2":  # Rehacer
        if pila_redo:
            texto_recuperado = pila_redo.pop()
            pila.append(texto_recuperado)
            print("\nSe rehízo:", texto_recuperado)
        else:
            print("\nNo hay elementos para rehacer.")

    elif opcion == "3":  # Salir del programa
        print("\n¡Gracias por usar el programa!")
        break

    else:
        print("\n¡ERROR: Digite valores válidos!")
