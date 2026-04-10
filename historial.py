import producto
from datetime import *
from productoBodega import *
import json
import os
import utilidades

def registrarHistorial(codigoProducto):

    historial = pedirDatos(codigoProducto)

    listaHistorial = utilidades.leerJson("data/historial.json")


    listaHistorial.append(historial)

    utilidades.escribirJson("data/historial.json",listaHistorial)

    print("Historial Agregado con Exito!!!")

def pedirDatos(codigoProducto):

        bodega = utilidades.validarBodega("Digite el numero de la Bodega(1. Central / 2. Norte / 3. Oriente): ")

        descripcion = utilidades.validarStr("Ingrese la descripcion: ")

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        stock = utilidades.validarEntero("Digite el stock: ")

        registrarProductoBodega(codigoProducto,bodega,stock)

        historial = crearDiccionario(bodega, codigoProducto, "Ingreso", stock, descripcion, fecha)


        return historial

def crearDiccionario(bodega,codigoProducto,tipo,stock,descripcion,fechaRegistro):
    return dict(
            codigoProducto = codigoProducto,
            codigoBodega = bodega,
            descripcion = descripcion,
            tipo = tipo,
            stock = stock,
            fechaRegistro = fechaRegistro
        )

def crearRegistro(bodega,codigoProducto,tipo,stock):

    descripcion = utilidades.validarStr("Ingrese la descripcion: ")

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    historial = crearDiccionario(bodega,codigoProducto,tipo,stock,descripcion,fecha)

    crearJson(historial)

    print("Producto Modificado con Exito!!!")


def crearJson(historial):

    listaHistorial = utilidades.leerJson("data/historial.json")

    listaHistorial.append(historial)

    utilidades.escribirJson("data/historial.json",listaHistorial)


def listarByProdBode():


        codigoProducto = utilidades.validarEntero("Ingrese el Codigo del Producto: ")


        codigoBodega = utilidades.validarBodega("Seleccione la Bodega(1. Centro / 2. Norte / 3. Oriente): ")


        if not producto.buscarExistencia(codigoProducto):

            listaHistorial = utilidades.leerJson("data/historial.json")

            for historial in listaHistorial:
                if historial["codigoProducto"] == codigoProducto and historial["codigoBodega"] == codigoBodega:
                    print(historial)
                    return
            print("El producto no se Encuentra en la bodega selecionada!!!")
            return
        else:
            print("Producto No Encontado!!!")