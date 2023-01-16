class Graph:
 
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed
    
        self.m_list_of_edges = []

    def add_edge(self, node1, node2, weight=1):        
        self.m_list_of_edges.append((node1, node2, weight))

        if not self.m_directed:
            self.m_list_of_edges.append((node2, node1, weight))

    def print_edge_list(self):
        num_of_edges = len(self.m_list_of_edges)
        for i in range(num_of_edges):
            print("edge ", i+1, ": ", self.m_list_of_edges[i])

graph = Graph(17, False)

graph.add_edge("Aldeeran", 'Endor', 5)
graph.add_edge("Dagobah", 'Scarif', 1)
graph.add_edge('Alderaan', 'planet1', 2)
graph.add_edge('planet1', 'planet2', 5)
graph.add_edge('planet3', 'Endor', 9)
graph.add_edge('Endor', 'Bespin', 4)
graph.add_edge('Hoth', 'tatooine', 20)
graph.add_edge("Kamino", 'Tatooine', 1)
graph.add_edge("Dagobah", 'Hoth', 12)
graph.add_edge('Kamiro', 'Naboo', 8)
graph.add_edge('planet1', 'planet3', 11)
graph.add_edge('planet1', 'planet6', 7)
graph.add_edge('planet5', 'planet1', 4)
graph.add_edge('Mustafar', 'Narif', 6)
graph.add_edge('planet2', 'planet5', 3)

graph.print_edge_list()

from collections import defaultdict
from heapq import *


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
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
                #print(prev)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return (float("inf"), [])

edges = graph.m_list_of_edges