#Código de tabla Hash
def crear_tabla(tamanio):
    """Crear una tabla hash vacia"""
    tabla = [None]*tamanio
    return tabla

def cantidad_elementos(tabla):
    """Devuelve la cantidad de elementos en la tabla"""
    return len(tabla) - tabla.count(None)

def funcion_hash(dato, tamanio_tabla):
    """Determina la posicion del dato en la tabla"""
    return len(str(dato).strip()) % tamanio_tabla

def agregar(tabla, dato, convert):
    posicion = funcion_hash(ord(dato), len(tabla))

    if (tabla[posicion] is None):
        if convert:
            tabla[posicion] = convert8chr(dato)
        else:
            tabla[posicion] = dato
    else:
        print("Se produjo una colision")
    
""" Si se produce dicha colisión, ejecuta función de sondeo para reubicar el elemento """

def buscar(tabla, buscado):
    """ Determina si un elemento existe en la tabla y determina su posición. """
    pos = None
    posicion = funcion_hash(buscado, len(tabla))
    if (tabla[posicion] is not None):
        
        if (buscado == tabla[posicion]):
            pos = posicion

        else:
            print("Aplicar función de sondeo")

    return pos

def quitar(tabla, dato):
    """Quita un elemento de la tabla cerrada si existe"""

    dato = None
    posicion = funcion_hash(dato, len(tabla))
    if (tabla[posicion] is not None):

        if (dato == tabla[posicion]):
            dato = tabla[posicion]
            tabla[posicion] = None

        else:
            print("Aplicar función de sondeo")
            """Para determinar si esta en otra posición y quitarlo"""

    return dato