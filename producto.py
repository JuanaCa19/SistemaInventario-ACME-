from historial import *
import json
import os


def registrar():
    listaProductos = []
    producto = pedirDatos()

    if producto is None:
        return

    if os.path.getsize("data/producto.json") > 0:
        with open("data/producto.json","r") as file:
            listaProductos = json.load(file)

    listaProductos.append(producto)

    with open("data/producto.json","w") as file:
        json.dump(listaProductos,file,indent=4)

    print("Producto Agregado con Exito!!!")

def pedirDatos():
    while True:
        try:
            codigoProducto = int(input("Digite elcodigo del Producto: "))
        except:
            print("Ingrese un dato numerico!!!")
            continue

        if buscarExistencia(codigoProducto):
            nombre = input("Digite el nombre del Producto: ")
            proveedor = input("Digite el proveedor del Producto: ")

            if(not(nombre.strip() and proveedor.strip())):
                print("No puede dejar datos Vacios")
                continue

            registrarHistorial(codigoProducto)

            producto = dict(
                Nombre=nombre,
                Codigo=codigoProducto,
                Proveedor=proveedor
            )
            return producto

def buscarExistencia(codigoIngresado):

    if os.path.getsize("data/producto.json") > 0:
        with open("data/producto.json","r") as file:
            listaProductos = json.load(file)

        for producto in listaProductos:
            if producto["Codigo"] == codigoIngresado:
                return False

        return True


def buscar():

    while True:
        try:
            codigoIngresado = int(input("Ingrese el codigo del Producto:"))
        except:
            print("Digite un dato numerico!!!")
            continue

        if os.path.getsize("data/producto.json") > 0:
            with open("data/producto.json","r") as file:
                listaProductos = json.load(file)

            for producto in listaProductos:
                if producto["Codigo"] == codigoIngresado:
                    print("Producto Encontrado!!!")
                    print("Codigo: ", producto["Codigo"])
                    print("Nombre: ", producto["Nombre"])
                    print("Proveedor: ", producto["Proveedor"])

                    buscarProductoBodega(codigoIngresado)
                    return
            print("Producto No encontrado")
            return

def ingresarProducto():
    while True:
        try:
            codigoIngresado = int(input("Digite el codigo del producto: "))
        except:
            print("Ingrese un dato numerico!!!")
            continue

        if not buscarExistencia(codigoIngresado):
            bodega = input("Ingrese la Bodega(1. Centro / 2. Norte / 3. Oriente)")
            if bodega not in ("1","2","3"):
                print("Seleccione una Bodega valida!!!")
                continue
            ingresarProductoBodega(bodega,codigoIngresado)
            return