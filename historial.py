import producto
from datetime import *
from productoBodega import *
import json
import os

def registrarHistorial(codigoProducto):

    historial = pedirDatos(codigoProducto)
    listaHistorial = []

    if os.path.getsize("data/historial.json") > 0:
        with open("data/historial.json", "r") as file:
            listaHistorial = json.load(file)

    listaHistorial.append(historial)

    with open("data/historial.json", "w") as file:
        json.dump(listaHistorial, file, indent=4)

    print("Historial Agregado con Exito!!!")

def pedirDatos(codigoProducto):

    bodega = input("Digite el numero de la Bodega(1. Central / 2. Norte / 3. Oriente): ")
    descripcion = input("Ingrese la descripcion: ")
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    tipo = input("Ingrese que tipo de transaccion es(Ingreso / Retiro): ")
    stock = int(input("Digite el stock: "))
    registrarProductoBodega(codigoProducto,bodega,stock)

    historial = dict(
        codigoProducto = codigoProducto,
        codigoBodega = bodega,
        descripcion = descripcion,
        tipo = tipo,
        stock = stock,
        fechaRegistro = fecha
    )

    return historial

def crearRegistro(bodega,codigoProducto,tipo,stock):

    descripcion = input("Ingrese la descripcion: ")
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    historial = dict(
        codigoProducto=codigoProducto,
        codigoBodega=bodega,
        descripcion=descripcion,
        tipo=tipo,
        stock=stock,
        fechaRegistro=fecha
    )
    crearJson(historial)

def crearJson(historial):

    listaHistorial = []

    if os.path.getsize("data/historial.json") > 0:
        with open("data/historial.json", "r") as file:
            listaHistorial = json.load(file)

    listaHistorial.append(historial)

    with open("data/historial.json", "w") as file:
        json.dump(listaHistorial, file, indent=4)

def listarByProdBode():
    codigoProducto = int(input("Ingrese el Codigo del Producto: "))
    codigoBodega = input("Seleccione la Bodega(1. Centro / 2. Norte / 3. Oriente): ")

    if not producto.buscarExistencia(codigoProducto):

        if os.path.getsize("data/historial.json") > 0:
            with open("data/historial.json", "r") as file:
                listaHistorial = json.load(file)

        for historial in listaHistorial:
            if historial["codigoProducto"] == codigoProducto and historial["codigoBodega"] == codigoBodega:
                print(historial)
