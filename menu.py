from producto import *
from productoBodega import *

def iniciar():
    op = 0
    while op != 6:
        op = mostrarMenu()
        ejecutarOpciones(op)

def mostrarMenu():
    print("""SISTEMA DE INVENTARIO
             1. Registrar Producto
             2. Modificar stock de Producto
             3. Buscar Producto
             4. Mostrar Historial
             5. Mostrar Reporte
             6. Salir
             Ingrese una opcion:""")
    op = input()
    return op

def ejecutarOpciones(op):
    if op == "1":
        registrar()
    elif op == "2":
        ingresarProducto()
    elif op == "3":
         buscar()
    elif op == "4":
          listarByProdBode()
    elif op == "5":
          generarReporte()
    elif op == "6":
        print("Cerrando Sistema de Inventario!!!")
    else:
        print("Opción Invalida!!!")


entrar = True
iniciar()