from datetime import *
import historial
import json
import os

import utilidades


def registrarProductoBodega(codigoProducto, codigoBodega,stock):

    productoBodega = pedirDatos(codigoProducto, codigoBodega,stock)

    listaProductoBodega = utilidades.leerJson("data/productoBodega.json")

    listaProductoBodega.append(productoBodega)

    utilidades.escribirJson("data/productoBodega.json",listaProductoBodega)

    print("Stock Agregado con Exito!!!")


def pedirDatos(codigoProducto, codigoBodega,stock):

    productoBodega = dict(
        codigoProducto = codigoProducto,
        codigoBodega = codigoBodega,
        stockProducto = stock
    )

    return productoBodega

def buscarProductoBodega(codigoIngresado):

    listaProductoBodega = utilidades.leerJson("data/productoBodega.json")

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

    stock = utilidades.validarEntero("Ingrese el Stock: ")

    if stockGuardado is None:
        productoBodega = pedirDatos(codigoProducto,bodega,stock)

        crearProductoBodega(productoBodega)

        historial.crearRegistro(bodega, codigoProducto, "Ingreso", stock)

        print("Producto Registrado en Nueva Bodega Exitosamente!!")

        return


    op = utilidades.validarModificacion("¿Que desea hacer? (1. Ingresar Producto / 2. Retirar Producto)")


    match op:
        case "1":

            stockGuardado +=stock

            historial.crearRegistro(bodega,codigoProducto,"Ingreso",stock)

        case "2":

            if stock <= stockGuardado:
                stockGuardado -= stock
                historial.crearRegistro(bodega, codigoProducto, "Retiro",stock)
            else:
                print("No hay Suficiente Stock!!!")
                return


    modificarStock(bodega, codigoProducto,stockGuardado)

def buscarStock(bodega,codigoProducto):

    listaProductoBodega = utilidades.leerJson("data/productoBodega.json")

    for productoBodega in listaProductoBodega:
        if productoBodega["codigoProducto"] == codigoProducto and productoBodega["codigoBodega"] == bodega:
            stock = productoBodega["stockProducto"]
            return stock


def modificarStock(bodega, codigoProducto,stockModificado):

    listaProductoBodega = utilidades.leerJson("data/productoBodega.json")

    for productoBodega in listaProductoBodega:
        if productoBodega["codigoProducto"] == codigoProducto and productoBodega["codigoBodega"] == bodega:
            productoBodega["stockProducto"] = stockModificado

    utilidades.escribirJson("data/productoBodega.json",listaProductoBodega)


def crearProductoBodega(productoBodega):

    listaProductoBodega = utilidades.leerJson("data/productoBodega.json")

    listaProductoBodega.append(productoBodega)

    utilidades.escribirJson("data/productoBodega.json",listaProductoBodega)


def generarReporte():

        codigoBodega = utilidades.validarBodega("Seleccione la Bodega(1. Centro / 2. Norte / 3. Oriente)")

        listaProductoBodega = utilidades.leerJson("data/productoBodega.json")

        totalProductos = 0
        totalProductosBodega = 0

        for productoBodega in listaProductoBodega:

            if productoBodega["codigoBodega"] == codigoBodega:
                totalProductosBodega += productoBodega["stockProducto"]
            totalProductos += productoBodega["stockProducto"]

        print("Cantidad de Productos en las Bodegas: ", totalProductos)

        match codigoBodega:
            case "1":
                mensaje = "Cantidad de Productos en la Bodega Central: " + str(totalProductosBodega)
                print(mensaje)
            case "2":
                mensaje = "Cantidad de Productos en la Bodega Norte: " + str(totalProductosBodega)
                print(mensaje)
            case "3":
                mensaje = "Cantidad de Productos en la Bodega Oriente: " + str(totalProductosBodega)
                print(mensaje)



        op = utilidades.validarModificacion("Desea Generar Un reporte.txt? (1. SI / 2. NO): ")

        if op == "1":

            with open("data/reporte.txt","a") as file:
                file.write("\n\nFecha: "+ str(datetime.now())+"\n"+"Cantidad de Productos en las Bodegas: "+ str(totalProductos)+"\n"+str(mensaje)+"\n")

            print("Reporte Generado con Exito!!!!")

        elif op == "2":

            print("Finalizando Reporte!!!")
