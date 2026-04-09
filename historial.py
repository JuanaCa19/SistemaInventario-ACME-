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
    while True:

        bodega = input("Digite el numero de la Bodega(1. Central / 2. Norte / 3. Oriente): ")
        if bodega not in ("1","2","3"):
            print("Seleccione una Bodega Valida!!!")
            continue

        descripcion = input("Ingrese la descripcion: ")

        if (not (descripcion.strip())):
            print("Descripcion No puede ser vacio")
            continue

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


        try:
            stock = int(input("Digite el stock: "))
        except:
            print("Digite un dato numerico!!!")
            continue

        registrarProductoBodega(codigoProducto,bodega,stock)

        historial = dict(
            codigoProducto = codigoProducto,
            codigoBodega = bodega,
            descripcion = descripcion,
            tipo = "Ingreso",
            stock = stock,
            fechaRegistro = fecha
        )

        return historial

def crearRegistro(bodega,codigoProducto,tipo,stock):
    while True:

        descripcion = input("Ingrese la descripcion: ")

        if not descripcion.strip():
            print("La descripcion no puede estar vacia!!!")
            continue

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
        print("Producto Modificado con Exito!!!")
        return

def crearJson(historial):

    listaHistorial = []

    if os.path.getsize("data/historial.json") > 0:
        with open("data/historial.json", "r") as file:
            listaHistorial = json.load(file)

    listaHistorial.append(historial)

    with open("data/historial.json", "w") as file:
        json.dump(listaHistorial, file, indent=4)

def listarByProdBode():
    while True:
        try:
            codigoProducto = int(input("Ingrese el Codigo del Producto: "))
        except:
            print("Digite un dato numerico!!!")
            continue

        codigoBodega = input("Seleccione la Bodega(1. Centro / 2. Norte / 3. Oriente): ")

        if codigoBodega not in ("1","2","3"):
            print("Seleccione una Bodega valida!!!")
            continue

        if not producto.buscarExistencia(codigoProducto):

            if os.path.getsize("data/historial.json") > 0:
                with open("data/historial.json", "r") as file:
                    listaHistorial = json.load(file)

            for historial in listaHistorial:
                if historial["codigoProducto"] == codigoProducto and historial["codigoBodega"] == codigoBodega:
                    print(historial)
                    return
            print("El producto no se Encuentra en la bodega selecionada!!!")
            return
        else:
            print("Producto No Encontado en la Bodega Seleccionada!!!")