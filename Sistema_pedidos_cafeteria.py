# Sistema de pedidos de cafetería

menu_cafeteria = ["Cafe", "Té", "Pan", "Jugo", "Galletas"]

pedidos = []

pila_deshacer = []


def agregar_pedido():
    nombre = input("\nDígite su nombre por favor: \n\n")
    pedido_actual = {"Nombre": nombre, "Productos": []}

    while True:
        print("\nMENÚ CAFETERIA\n")
        print("1. Café.")
        print("2. Té.")
        print("3. Pan.")
        print("4. Jugo.")
        print("5. Galletas.")
        print("\n6. Salir.")

        try:
            opcion = int(input("\nDigite la opción que desea añadir a su carrito:\n"))

            if 1 <= opcion <= 5:
                pedido_actual["Productos"].append(menu_cafeteria[opcion - 1])
                print(f"\n¡Se añadió con éxito {menu_cafeteria[opcion - 1]} al carrito!\n")

            elif opcion == 6:
                print("\n¡Gracias por elegir nuestros productos!\n")
                pedidos.append(pedido_actual)  # Se guarda el pedido en la lista de pedidos
                pila_deshacer.append(pedido_actual.copy())  # Se almacena una copia para deshacer
                break

            else:
                print("\n¡ERROR: opción incorrecta, vuelva a intentarlo\n")

        except ValueError:
            print("\nERROR: Datos no válidos. Vuelva a intentarlo\n")


def deshacer_pedido():
    if pedidos:
        ultimo_pedido = pedidos.pop()  
        pila_deshacer.append(ultimo_pedido) 
        print("\n ¡Se deshizo el último pedido correctamente!\n")
    else:
        print("\n No hay acciones para deshacer.\n")


def mostrar_pedidos():
    if pedidos:
        print("\n Lista de pedidos registrados:\n")
        for i, pedido in enumerate(pedidos, 1):
            print(f"{i}. Cliente: {pedido['Nombre']}")
            for producto in pedido["Productos"]:
                print(f"   - {producto}")
    else:
        print("\n¡ No hay pedidos registrados aún !")


def eliminar_producto():
    if not pedidos:
        print("\n¡ No hay pedidos registrados aún !\n")
        return

    mostrar_pedidos()

    try:
        pedido_indice = int(input("\nIngrese el número de pedido del cual desea eliminar un producto:\n")) - 1

        if 0 <= pedido_indice < len(pedidos):
            pedido = pedidos[pedido_indice]

            if not pedido["Productos"]:
                print("\nEste pedido no tiene productos para eliminar.\n")
                return

            prod_eliminar = input("\nIngrese el producto que desea eliminar del carrito:\n")

            if prod_eliminar in pedido["Productos"]:
                pedido["Productos"].remove(prod_eliminar)
                print(f"\n¡Se eliminó correctamente {prod_eliminar} del carrito!\n")
            else:
                print("\n¡No se encuentra este producto en el carrito!\n")

        else:
            print("\nNúmero de pedido inválido.\n")

    except ValueError:
        print("\n¡ERROR: Ingrese un número válido!\n")


while True:
    print("\n M E N Ú   P R I N C I P A L \n")
    print("1. Agregar pedido")
    print("2. Deshacer pedido")
    print("3. Mostrar pedidos")
    print("4. Eliminar producto de carrito")
    print("5. Salir")

    try:
        opcion = int(input("\nDigite la opción que necesita:\n"))

        if opcion == 1:
            agregar_pedido()
        elif opcion == 2:
            deshacer_pedido()
        elif opcion == 3:
            mostrar_pedidos()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            print("\n¡Gracias por preferirnos!\n")
            break
        else:
            print("\n¡ERROR: Opción inválida, intente de nuevo!\n")

    except ValueError:
        print("\n¡ERROR: Ingrese valores válidos!\n")
