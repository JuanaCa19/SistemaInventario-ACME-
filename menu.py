from producto import *
from productoBodega import *

def iniciar():
    op = "0"
    while op != "6":
        op = mostrarMenu()
        ejecutarOpciones(op)

def mostrarMenu():
    op = input("""SISTEMA DE INVENTARIO
             1. Registrar Producto
             2. Modificar stock de Producto
             3. Buscar Producto
             4. Mostrar Historial
             5. Mostrar Reporte
             6. Salir
             Ingrese una opcion:""")
    return op

def ejecutarOpciones(op):
    match op:
        case "1":
            registrar()
        case "2":
            ingresarProducto()
        case "3":
             buscar()
        case "4":
            listarByProdBode()
        case "5":
            generarReporte()
        case "6":
            print("Cerrando Sistema de Inventario!!!")
        case _:
            print("Opción Invalida!!!")


iniciar()