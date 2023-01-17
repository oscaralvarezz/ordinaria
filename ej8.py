#Creamos la clase
class Grafo:
 
    def __init__(self, num_nodos, dirigido=True):
        self.num_nodos = num_nodos
        self.dirigido = dirigido
    
        self.lista_de_vertices = []

    def añadir_vertices(self, nodo1, nodo2, peso=1):        
        self.lista_de_vertices.append((nodo1, nodo2, peso))

        if not self.dirigido:
            self.lista_de_vertices.append((nodo2, nodo1, peso))

    def lista_vertices(self):
        num_vertices = len(self.lista_de_vertices)
        for i in range(num_vertices):
            print("vértice", i+1, ": ", self.lista_de_vertices[i])

grafo = Grafo(17, False)

#añadimos los vértices al grafo
grafo.añadir_vertices("Aldeeran", 'Endor', 5)
grafo.añadir_vertices("Dagobah", 'Scarif', 1)
grafo.añadir_vertices('Alderaan', 'planeta1', 2)
grafo.añadir_vertices('planeta1', 'planeta2', 5)
grafo.añadir_vertices('planeta3', 'Endor', 9)
grafo.añadir_vertices('Endor', 'Bespin', 4)
grafo.añadir_vertices('Hoth', 'tatooine', 20)
grafo.añadir_vertices("Kamino", 'Tatooine', 1)
grafo.añadir_vertices("Dagobah", 'Hoth', 12)
grafo.añadir_vertices('Kamiro', 'Naboo', 8)
grafo.añadir_vertices('planeta1', 'planeta3', 11)
grafo.añadir_vertices('planeta1', 'planeta6', 7)
grafo.añadir_vertices('planeta5', 'planeta1', 4)
grafo.añadir_vertices('Mustafar', 'Narif', 6)
grafo.añadir_vertices('planeta2', 'planeta5', 3)

grafo.lista_vertices()

from heapq import *
from collections import defaultdict

#hacemos el algoritmo de dijkstra para hallar la ruta más corta.
def dijkstra(vertices, f, t):
    g = defaultdict(list)
    for l, r, c in vertices:
        g[l].append((c, r))
    print(g)
    q, seen, mins = [(0, f, [])], set(), {f: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = [v1] + path
            if v1 == t:
                return (cost, path)
            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return (float("inf"), [])

#Finalmente, mostramos por pantalla los vértices y su longitud
vertices = grafo.lista_de_vertices