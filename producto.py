from historial import *
import json
import os
import utilidades


def registrar():

    producto = pedirDatos()

    if producto is None:
        return

    listaProductos = utilidades.leerJson("data/producto.json")

    listaProductos.append(producto)

    utilidades.escribirJson("data/producto.json",listaProductos)

    print("Producto Agregado con Exito!!!")

def pedirDatos():

    codigoProducto = utilidades.validarEntero("Digite elcodigo del Producto: ")

    if not buscarExistencia(codigoProducto):
        print("Producto Ya Registrado con este Codigo: ",codigoProducto)
        return

    nombre = utilidades.validarStr("Digite el nombre del Producto: ")

    proveedor = utilidades.validarStr("Digite el proveedor del Producto: ")


    registrarHistorial(codigoProducto)

    producto = dict(
        Nombre=nombre,
        Codigo=codigoProducto,
        Proveedor=proveedor
    )
    return producto



def buscarExistencia(codigoIngresado):

    listaProductos = utilidades.leerJson("data/producto.json")

    for producto in listaProductos:
        if producto["Codigo"] == codigoIngresado:
            return False

    return True


def buscar():

    codigoIngresado = utilidades.validarEntero("Ingrese el codigo del Producto:")

    listaProductos = utilidades.leerJson("data/producto.json")

    for producto in listaProductos:
        if producto["Codigo"] == codigoIngresado:
            print("Producto Encontrado!!!")
            print("Codigo: ", producto["Codigo"])
            print("Nombre: ", producto["Nombre"])
            print("Proveedor: ", producto["Proveedor"])

            buscarProductoBodega(codigoIngresado)
            return
    print("Producto No encontrado")

def ingresarProducto():

    codigoIngresado = utilidades.validarEntero("Digite el codigo del producto: ")

    if buscarExistencia(codigoIngresado):
        print("El Producto no se encuentra registrado!!!")
        return

    bodega = utilidades.validarBodega("Ingrese la Bodega(1. Centro / 2. Norte / 3. Oriente)")

    ingresarProductoBodega(bodega,codigoIngresado)
