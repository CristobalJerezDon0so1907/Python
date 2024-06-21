from misfunciones import limpiar,printR,printV,printA,menu, agregar_producto,mostrar_inventario, vender_producto,guardar_inventario,cargar_inventario


while True:
    limpiar()
    menu()
    opcion = int(input("Seleccione : "))
    if opcion==0:
        break
    elif opcion==1:
        printA("Agregar un nuevo producto al inventario")
        nombre = input("Ingrese nombre del producto : ")
        precio = float(input("Ingrese el precio del producto : "))
        cantidad = int(input("Ingrese la cantidad del producto : "))
        inventario = agregar_producto(inventario,nombre,precio,cantidad)
        printV("Producto agregado con existo")
    elif opcion==2:
        printA("Mostrar el inventario")
        def mostrar_inventario():
            mostrar_inventario(inventario)
    elif opcion==3:
        printA("Vender un producto")
        nombre = input("Ingrese el nombre del producto a vender : ")
        cantidad = int(input("Ingrese la cantidad del producto a vender : "))
        total = vender_producto(inventario,nombre,cantidad)
        if isinstance(total,str):
            print(total)
            printA(f"TOTAL DE LA VENTA {total}")
        else:
            printR("Ningun producto se ha vendido")
    elif opcion==4:
        print("Cargar el inventario desde un archivo CSV")
        def cargar_inventario():
            archivo = input("Ingrese el nombre del archivo donde se guardara el inventario : ")
            inventario = cargar_inventario(archivo)
            print("Inventario cargado con existo")
    elif opcion==5:
        printA("Guardar el inventario en un archivo CSV")
        guardar_inventario()
    else:
        print("❌ opcion no valida ❌")
