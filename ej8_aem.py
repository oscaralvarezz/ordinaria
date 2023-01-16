class Node:
  def __init__(self, nombre):
    self.nombre = nombre
    self.vecino = {}
    
  def agregar_nodo(self, nodo, peso):
    self.vecino[nodo] = peso

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []
        self.padre = [i for i in range(vertices)]
        self.rango = [0 for i in range(vertices)]
        self.nombre_a_vertice = {}
        self.vertice_a_nombre = {}


    def agregar_arista(self, u, v, w):
        if u not in self.nombre_a_vertice:
            vertice = len(self.nombre_a_vertice)
            self.nombre_a_vertice[u] = vertice
            self.vertice_a_nombre[vertice] = u
        if v not in self.nombre_a_vertice:
            vertice = len(self.nombre_a_vertice)
            self.nombre_a_vertice[v] = vertice
            self.vertice_a_nombre[vertice] = v
        u = self.nombre_a_vertice[u]
        v = self.nombre_a_vertice[v]
        self.grafo.append((u, v, w))

    def encontrar(self, i):
        if self.padre[i] == i:
            return i
        return self.encontrar(self.padre[i])

    def unir(self, x, y):
        xroot = self.encontrar(x)
        yroot = self.encontrar(y)
        if self.rango[xroot] < self.rango[yroot]:
            self.padre[xroot] = yroot
        elif self.rango[xroot] > self.rango[yroot]:
            self.padre[yroot] = xroot
        else:
            self.padre[yroot] = xroot
            self.rango[xroot] += 1

    def kruskal(self):
        resultado = []
        i, e = 0, 0
        self.grafo = sorted(self.grafo, key=lambda x: x[2])
        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.encontrar(u)
            y =self.encontrar(v)
            if x != y:
                e = e + 1
                resultado.append((u, v, w))
                self.unir(x, y)
        return resultado

    def obtener_peso_arbol(self):
        arbol = self.kruskal()
        peso = 0
        for u, v, w in arbol:
            peso += w
        return peso

    def obtener_arbol(self):
        arbol = self.kruskal()
        resultado = []
        for u, v, w in arbol:
            resultado.append((self.vertice_a_nombre[u], self.vertice_a_nombre[v], w))
        return resultado

def main2():
    grafo = Grafo(5)

    grafo.agregar_arista("Tatooine", "Dagobah", 13)
    grafo.agregar_arista("Tatooine", "Hoth", 123)
    grafo.agregar_arista("Tatooine", "Naboo", 143)
    grafo.agregar_arista("Tatooine", "Aldera", 153)

    grafo.agregar_arista("Dagobah", "Naboo", 160)
    grafo.agregar_arista("Dagobah", "Hoth", 15)
    grafo.agregar_arista("Dagobah", "Aldera", 2124)

    grafo.agregar_arista("Dagobah", "Aldera", 2412)
    grafo.agregar_arista("Dagobah", "Aldera", 221)
    grafo.agregar_arista("Dagobah", "Aldera", 152)
    grafo.agregar_arista("Dagobah", "Aldera", 562)

    
    # Sacar el arbol de expansion minima
    arbol = grafo.obtener_arbol()

    for u, v, w in arbol:
        print(f"{u} - {v}: {w} distancia")

    peso = sum(borde[2] for borde in arbol)

    # Ahora podemos imprimir el peso del árbol de expansión máxima
    print(f"Peso del árbol de expansión minimo: {peso}")