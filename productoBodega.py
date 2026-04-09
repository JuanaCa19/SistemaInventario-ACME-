from datetime import *
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

    if os.path.getsize("data/producto.json") > 0:
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
    while True:

        op = input("¿Que desea hacer? (1. Ingresar Producto / 2. Retirar Producto)")

        if op not in ("1","2"):
            print("Selecciona una opcion Correcta!!!")
            continue

        if op =="1":

            try:
                stock = int(input("Ingrese el stock a sumar: "))
            except:
                print("Ingrese un dato numerico!!!")
                continue

            stockGuardado +=stock

            historial.crearRegistro(bodega,codigoProducto,"Ingreso",stock)

        elif op=="2":

            try:
                stock = int(input("Ingrese el stock a restar: "))
            except:
                print("Ingrese un dato numerico!!!")
                continue

            if stock <= stockGuardado:
                stockGuardado -= stock
                historial.crearRegistro(bodega, codigoProducto, "Retiro",stock)
            else:
                print("No hay Suficiente Stock!!!")
                continue


        modificarStock(bodega, codigoProducto,stockGuardado)
        return

def buscarStock(bodega,codigoProducto):

    if os.path.getsize("data/producto.json") > 0:
        with open("data/productoBodega.json","r") as file:
            listaProductoBodega = json.load(file)

        for productoBodega in listaProductoBodega:
            if productoBodega["codigoProducto"] == codigoProducto and productoBodega["codigoBodega"] == bodega:
                stock = productoBodega["stockProducto"]
                return stock


def modificarStock(bodega, codigoProducto,stockModificado):

    if os.path.getsize("data/producto.json") > 0:
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
    while True:
        codigoBodega = input("Seleccione la Bodega(1. Centro / 2. Norte / 3. Oriente)")

        if codigoBodega not in ("1", "2", "3"):
            print("Seleccione una Bodega valida!!!")
            continue

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
            mensaje="Cantidad de Productos en la Bodega Central: "+ str(totalProductosBodega)
            print(mensaje)
        elif codigoBodega == "2":
            mensaje = "Cantidad de Productos en la Bodega Norte: " + str(totalProductosBodega)
            print(mensaje)
        elif codigoBodega == "3":
            mensaje = "Cantidad de Productos en la Bodega Oriente: " + str(totalProductosBodega)
            print(mensaje)
        else:
            print("Ingrese un codigo de bodega Correcto!!!")
            return

        while True:
            print("Desea Generar Un reporte.txt? (1. SI / 2. NO)")
            op = input()
            if op == "1":
                with open("data/reporte.txt","a") as file:
                    file.write("\n\nFecha: "+ str(datetime.now())+"\n"+"Cantidad de Productos en las Bodegas: "+ str(totalProductos)+"\n"+str(mensaje)+"\n")
                print("Reporte Generado con Exito!!!!")
                return
            elif op == "2":
                print("Finalizando Reporte!!!")
                return
            else:
                print("Ingrese una Opcion Valida")