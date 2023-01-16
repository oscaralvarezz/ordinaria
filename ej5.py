def mochila(pesos, valores, capacidad):
    n = len(pesos)
    tabla = [[0] * (capacidad + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacidad + 1):
            if pesos[i - 1] > j:
                tabla[i][j] = tabla[i - 1][j]
            else:
                tabla[i][j] = max(tabla[i - 1][j], tabla[i - 1][j - pesos[i - 1]] + valores[i - 1])
    return tabla[n][capacidad]



if __name__=="__main__":
    pesos = [12, 23, 11, 15, 7]
    valores =  [103, 60, 70, 5, 15] 
    capacidad = 100
    resultado = mochila(pesos, valores, capacidad)
    print("El valor máximo que se puede llevar es: " , resultado)