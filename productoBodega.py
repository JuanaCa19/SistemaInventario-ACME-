import historial
import json
import os



def registrarProductoBodega(codigoProducto, codigoBodega,stock):

    productoBodega = pedirDatos(codigoProducto, codigoBodega,stock)
    listaProductoBodega = []

    if os.path.getsize("data/productoBodega.json") > 0:
        with open("data/productoBodega.json", "r") as file:
            listaProductoBodega = json.load(file)

    listaProductoBodega.append(productoBodega)

    with open("data/productoBodega.json", "w") as file:
        json.dump(listaProductoBodega, file, indent=4)

    print("Stock Agregado con Exito!!!")


def pedirDatos(codigoProducto, codigoBodega,stock):

    productoBodega = dict(
        codigoProducto = codigoProducto,
        codigoBodega = codigoBodega,
        stockProducto = stock
    )

    return productoBodega

def buscarProductoBodega(codigoIngresado):

    with open("data/productoBodega.json", "r") as file:
        listaProductoBodega = json.load(file)

    for productoBodega in listaProductoBodega:

        if productoBodega["codigoProducto"] == codigoIngresado:

            if productoBodega["codigoBodega"] == "1":
                print("Bodega : Centro")
            elif productoBodega["codigoBodega"] == "2":
                print("Bodega : Norte")
            elif productoBodega["codigoBodega"] == "3":
                print("Bodega : Oriente")

            print("Stock : ",productoBodega["stockProducto"])

def ingresarProductoBodega(bodega,codigoProducto):


    stockGuardado = buscarStock(bodega,codigoProducto)

    if stockGuardado is None:
        productoBodega = pedirDatos(codigoProducto,bodega)
        crearProductoBodega(productoBodega)
        print("Producto Registrado en Nueva Bodega Exitosamente!!")
        return

    op = input("¿Que desea hacer? (1. Ingresar Producto / 2. Retirar Producto)")

    if op =="1":
        stock = int(input("Ingrese el stock a sumar: "))
        stockGuardado +=stock
        historial.crearRegistro(bodega,codigoProducto,"Ingreso",stock)
    elif op=="2":
        stock = int(input("Ingrese el stock a restar: "))
        if stock <= stockGuardado:
            stockGuardado -= stock
            historial.crearRegistro(bodega, codigoProducto, "Retiro",stock)
        else:
            print("No hay Suficiente Stock!!!")
            return
    else:
        print("Ingrese una Opcion valida!!!")
        return

    modificarStock(bodega, codigoProducto,stockGuardado)

def buscarStock(bodega,codigoProducto):
    with open("data/productoBodega.json","r") as file:
        listaProductoBodega = json.load(file)

    for productoBodega in listaProductoBodega:
        if productoBodega["codigoProducto"] == codigoProducto and productoBodega["codigoBodega"] == bodega:
            stock = productoBodega["stockProducto"]
            return stock


def modificarStock(bodega, codigoProducto,stockModificado):
    with open("data/productoBodega.json", "r") as file:
        listaProductoBodega = json.load(file)

    for productoBodega in listaProductoBodega:
        if productoBodega["codigoProducto"] == codigoProducto and productoBodega["codigoBodega"] == bodega:
            productoBodega["stockProducto"] = stockModificado


    with open("data/productoBodega.json", "w") as file:
        json.dump(listaProductoBodega,file,indent=4)

def crearProductoBodega(productoBodega):

    if os.path.getsize("data/productoBodega.json") > 0:
        with open("data/productoBodega.json", "r") as file:
            listaProductoBodega = json.load(file)

    listaProductoBodega.append(productoBodega)

    with open("data/productoBodega.json", "w") as file:
        json.dump(listaProductoBodega, file, indent=4)

def generarReporte():

    codigoBodega = input("Seleccione la Bodega(1. Centro / 2. Norte / 3. Oriente)")

    if os.path.getsize("data/productoBodega.json") > 0:
        with open("data/productoBodega.json", "r") as file:
            listaProductoBodega = json.load(file)

        totalProductos = 0
        totalProductosBodega = 0
        for productoBodega in listaProductoBodega:
            if productoBodega["codigoBodega"] == codigoBodega:
                totalProductosBodega += productoBodega["stockProducto"]
            totalProductos += productoBodega["stockProducto"]

    print("Cantidad de Productos en las Bodegas: ", totalProductos)
    if codigoBodega == "1":
        print("Cantidad de Productos en la Bodega Central: ", totalProductosBodega)
    elif codigoBodega == "2":
        print("Cantidad de Productos en la Bodega Central: ", totalProductosBodega)
    elif codigoBodega == "2":
        print("Cantidad de Productos en la Bodega Central: ", totalProductosBodega)
    else:
        print("Ingrese un codigo de bodega Correcto!!!")