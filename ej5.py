def main():
    #creamos una función para determinar el valor máximo de la mochila según valores y pesos de los objetos.
    def mochila(pesos, valores, capacidad):
        z = len(pesos)
        tabla = [[0] * (capacidad + 1) for _ in range(z + 1)]
        for i in range(1, z + 1):
            for j in range(1, capacidad + 1):
                if pesos[i - 1] > j:
                    tabla[i][j] = tabla[i - 1][j]
                else:
                    tabla[i][j] = max(tabla[i - 1][j], tabla[i - 1][j - pesos[i - 1]] + valores[i - 1])
        return tabla[z][capacidad]

    #Asignamos los pesos y valor al correspondiente objeto, y también la capacidad máxima de la mochila
    pesos = [12, 23, 11, 15, 7]
    valores =  [103, 60, 70, 5, 15] 
    capacidad_max = 60
    resultado = mochila(pesos, valores, capacidad_max)

    #mostramos el valor final de la mochila.
    print("El valor máximo de los objetos que se pueden llevar en la mochila es de:",resultado)

if __name__=="__main__":
    main()