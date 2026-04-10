import json
import os
from App.Utilidad import ruta

def validarEntero(mensaje):
    while True:

        try:
            numero = int(input(mensaje))

            if numero < 0:
                print("Digite un valor positivo")
                continue
            else:
                return numero
        except (ValueError,TypeError):
            print("Digite un dato numerico!!!")
            continue

def validarStr(mensaje):
    while True:
        texto = str(input(mensaje))
        if not texto.strip():
            print("No se permiten valores vacios!!!")
            continue
        elif len(texto) > 100:
            print("El texto digitado no puede ser tan grande")
            continue
        else:
            return texto

def validarBodega(mensaje):
    while True:
        bodega = input(mensaje)

        if bodega not in ("1","2","3"):
            print("Seleccione una Bodega Valida!!!")
            continue
        else:
            return bodega

def validarModificacion(mensaje):
    while True:
        op = input(mensaje)
        if op not in ("1", "2"):
            print("Selecciona una opcion Correcta!!!")
            continue
        return op

def leerJson(rutaArchivo):
    if os.path.getsize(ruta.ruta+rutaArchivo) > 0:
        with open(ruta.ruta+rutaArchivo, "r") as file:
            lista = json.load(file)
            return lista
    else:
        print("JSON Vacio")
        return []

def escribirJson(rutaArchivo,lista):

    with open(ruta.ruta+rutaArchivo, "w") as file:
        json.dump(lista, file, indent=4)
