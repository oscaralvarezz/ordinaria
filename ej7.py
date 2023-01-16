# El codigo para el codigo Huffman ha sido sacado del ejercicio que hicimos previamente en clase.

class Nodo():
    def __init__(self, izq=None, der=None):
        self.izq= izq
        self.der=der
    
    def hijo(self):
        return self.izq, self.der

# Creamos el arbol binario
def arbol(dict_frec):

    # Primero convertimos el diccionario de frecuencias en una lista
    list_frec= list(dict_frec)

    # Generamos los nodos del arbol binario
    while len(list_frec) > 1:
        val1, frec1 =list_frec[0]
        val2, frec2 =list_frec[1]
        nodo=Nodo(val1, val2)
        list_frec.append((nodo, frec1+frec2))
        list_frec= sorted(list_frec, key=lambda x: x[1], reverse=False)
        list_frec= list_frec[2:]
    return list_frec[0]

# Implementamos la codificacion de Huffman y calculamos la tabla de codificacion
def huffman(arbol, codigo=''):
    if type(arbol) is str:
        return {arbol: codigo}

    # Creamos diccionario para las claves de huffman por cada nodo(0 y 1)
    izq, der = arbol.hijo()
    dict_huffman = dict()
    dict_huffman.update(huffman(izq, codigo + '0'))
    dict_huffman.update(huffman(der, codigo + '1'))
    
    return dict_huffman

# Codificamos el mensaje
def codificar(cadena, huff):
    codigo=''
    for letra in cadena:
        codigo= codigo + huff[letra]
    return codigo

# Decodificamos el mensaje cogiendo el arbol previamente calculado
def decodificar(codificado, raiz, nodo, decodificado=''):

    # Iteramos sobre los nodos y sacamos el mensaje decodificado
    for valor in codificado:
        if valor == '0':
            nodo= nodo.izq
        else:
            nodo= nodo.der
        if type(nodo) is str:
            decodificado= decodificado + nodo
            nodo= raiz
    return decodificado

# Funcion que devuelve el peso de cada frecuencia sobre el total dada una cadena o una tabla de frecuencias
def ordenar(cadena):
    # Creamos un diccionario para almacenar los valores en caso de que hagamos la tabla de frecuencias en base a 
    # un string y no a un diccionario. 
    dict_contador = dict()
    
    # Si el input que le pasamos no es un diccionario creara una tabla de frecuencias en base a la cadena,
    # de lo contrario tomara directamente el diccionario como argumento
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

    # Iteramos sobre cada valor del diccionario para sacar su peso proporcional en la tabla
    for letra in dict_contador:
        dict_frecuencias[letra]=dict_contador[letra]/suma_total

    # Ordenamos el nuevo diccionario 
    frecuencias_ordenadas=sorted(dict_frecuencias.items(), key=lambda x: x[1], reverse=False)
    return frecuencias_ordenadas

if __name__=="__main__":
    # Cogemos la cadena de texto
    frecuencias = {"a":0.2,"f":0.17,"1":0.13,"3":0.21,"0":0.05,"m":0.09,"t":0.15}

    # Ordenamos la tabla de valoresm, sacar peso de cada valor
    peso_frec = ordenar(frecuencias)
    
    #Creamos el arbol
    arbol = arbol(peso_frec)

    #Añadimos los valores de Huffman
    huff=huffman(arbol[0])

    # Codificamos el mensaje
    mensaje_codificado = codificar(frecuencias, huff)
    print(f"El mensaje codificado es: {mensaje_codificado}")

    # Decodificamos el mensaje
    mensaje_decodificado = decodificar(mensaje_codificado, arbol[0], arbol[0])
    print(f"El mensaje decodificado es: {mensaje_decodificado}")