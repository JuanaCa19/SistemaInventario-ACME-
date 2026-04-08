from historial import *
import json
import os


def registrar():
    listaProductos = []
    producto = pedirDatos()

    if producto is None:
        print("Ya existe un producto con ese Codigo")
        registrar()
        return

    if os.path.getsize("data/producto.json") > 0:
        with open("data/producto.json","r") as file:
            listaProductos = json.load(file)

    listaProductos.append(producto)

    with open("data/producto.json","w") as file:
        json.dump(listaProductos,file,indent=4)

    print("Producto Agregado con Exito!!!")

def pedirDatos():
    codigoProducto = int(input("Digite elcodigo del Producto: "))

    if buscarExistencia(codigoProducto):
        nombre = input("Digite el nombre del Producto: ")
        proveedor = input("Digite el proveedor del Producto: ")

        registrarHistorial(codigoProducto)

        producto = dict(
            Nombre=nombre,
            Codigo=codigoProducto,
            Proveedor=proveedor
        )
        return producto

def buscarExistencia(codigoIngresado):

    with open("data/producto.json","r") as file:
        listaProductos = json.load(file)

    for producto in listaProductos:
        if producto["Codigo"] == codigoIngresado:
            return False

    return True

def listar():
    with open("data/producto.json","r") as file:
        print(file.read())

def buscar():
    codigoIngresado = int(input("Ingrese el codigo del Producto:"))

    with open("data/producto.json","r") as file:
        listaProductos = json.load(file)

    for producto in listaProductos:
        if producto["Codigo"] == codigoIngresado:
            print("Producto Encontrado!!!")
            print("Codigo: ", producto["Codigo"])
            print("Nombre: ", producto["Nombre"])
            print("Proveedor: ", producto["Proveedor"])

            buscarProductoBodega(codigoIngresado)

def ingresarProducto():

    codigoIngresado = int(input("Digite el codigo del producto: "))

    if not buscarExistencia(codigoIngresado):
        bodega = input("Ingrese la Bodega(1. Centro / 2. Norte / 3. Oriente)")
        ingresarProductoBodega(bodega,codigoIngresado)