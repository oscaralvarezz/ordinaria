# El codigo Huffman ha sido extraído del ejercicio que hecho en clase.
class Nodo():
    def __init__(self, izq=None, der=None):
        self.izq= izq
        self.der=der
    
    def hijo(self):
        return self.izq, self.der

#Creamos el arbol binario
def arbol(dict_frec):

    #Inicialmente convertimos en una lista el diccionario de frecuencias.
    list_frec= list(dict_frec)

    #Posteriormente generamos los nodos del arbol binario
    while len(list_frec) > 1:
        val1, frec1 =list_frec[0]
        val2, frec2 =list_frec[1]
        nodo=Nodo(val1, val2)
        list_frec.append((nodo, frec1+frec2))
        list_frec= sorted(list_frec, key=lambda x: x[1], reverse=False)
        list_frec= list_frec[2:]
    return list_frec[0]

#Ahora implementamos la codificación de Huffman y se "calcula" la tabla de codificación
def huffman(arbol, codigo=''):
    if type(arbol) is str:
        return {arbol: codigo}

    #Creamos un diccionario para las claves de Huffman para cada nodo (0 y 1)
    izq, der = arbol.hijo()
    dict_huffman = dict()
    dict_huffman.update(huffman(izq, codigo + '0'))
    dict_huffman.update(huffman(der, codigo + '1'))
    
    return dict_huffman

#Creamos una función para codificar el mensaje.
def codificar(cadena, huff):
    codigo = ''
    for letra in cadena:
        codigo= codigo + huff[letra]
    return codigo

#Creamos ahora la función para decodificar el mensaje cogiendo el árbol realizado.
def decodificar(codificado, raiz, nodo, decodificado=''):
    #Ahora iteramos sobre los nodos y exrtraemos el mensaje decodificado
    for valor in codificado:
        if valor == '0':
            nodo= nodo.izq
        else:
            nodo= nodo.der
        if type(nodo) is str:
            decodificado= decodificado + nodo
            nodo= raiz
    return decodificado

'''La siguiente función devuelve el peso de cada frecuencia sobre 
el total dado a una cadena o una tabla de frecuencias'''

def ordenar(cadena):
    #Hacemos un diccionario para almacenar los valores por si hacemos la tabla de frecuencias en base a 
    #un string (no a un diccionario)
    dict_contador = dict()
    
    '''Si el input que hacemos no es un diccionario, creara una tabla de frecuencias en base al string,
    de lo contrario, tomará directamente el diccionario como el argumento'''
    if type(cadena) is not dict:
        for letra in set(cadena):
            dict_contador[letra] = []

        for letra in cadena:
            dict_contador[letra].append(1)
    
        for letra in dict_contador:
            dict_contador[letra] = sum(dict_contador[letra])
    else:
        dict_contador = cadena
    
    suma_total= sum(dict_contador.values())
    dict_frecuencias = dict()

    #Iteramos sobre cada valor del diccionario para sacar su peso proporcional en la tabla
    for letra in dict_contador:
        dict_frecuencias[letra]=dict_contador[letra]/suma_total

    #Ordenamos el diccionario nuevo
    frecuencias_ordenadas=sorted(dict_frecuencias.items(), key=lambda x: x[1], reverse=False)
    return frecuencias_ordenadas

#Cogemos la cadena de texto
frecuencias = {"a":0.2,"f":0.17,"1":0.13,"3":0.21,"0":0.05,"m":0.09,"t":0.15}

# Ordenamos la tabla de valores para sacar el peso de cada valor.
peso_frec = ordenar(frecuencias)
    
#Creamos el nuevo árbol
arbol = arbol(peso_frec)

#Añadimos los valores de Huffman
huff=huffman(arbol[0])

#Codificamos el mensaje
mensaje_codificado = codificar(frecuencias, huff)
print(f"El mensaje codificado es: {mensaje_codificado}")

#Decodificamos el mensaje
mensaje_decodificado = decodificar(mensaje_codificado, arbol[0], arbol[0])
print(f"El mensaje decodificado es: {mensaje_decodificado}")