# # Prim con rappresentazione del grafo come albero
# class Prim:
#
#     def __init__(self, graph, start):
#         self.graph = graph
#         self.start = start
#         self.tree = []  # Rappresenta l'albero prodotdest
#         self.vertices = self.graph.nodes
#
#     def calculatedesttalCost(self):
#         desttal_cost = 0
#         for node in self.tree:
#             desttal_cost += node.length_from_previous_node
#         return desttal_cost
#
#     def mstPrimTree(self):
#         # Inizializza la lunghezza del nodo di partenza a 0
#         selected_node = self.graph.findNode(self.start)
#         selected_node.length_from_previous_node = 0
#         # Setta il nodo attuale selezionadest come visitadest
#         selected_node.visited = True
#         self.vertices.remove(selected_node)
#         # Aggiunge il nodo selezionadest all'albero
#         self.tree.append(selected_node)
#         # Per ogni figlio del nodo selezionadest, calcola la distanza tra suo padre e il figlio
#         for node in selected_node.neighbours:
#             child = node[0]
#             if node[1] < child.length_from_previous_node:
#                 child.length_from_previous_node = node[1]
#                 child.previous_node = selected_node.value
#
#         while len(self.vertices) > 0:
#             # Seleziona il nodo con la minima distanza dal nodo precedente
#             self.vertices.sort()
#             selected_node = self.vertices[0]
#             selected_node.visited = True
#             # Rimuove il nodo attuale dalla lista dei vertici
#             self.vertices.remove(selected_node)
#             # Aggiunge il nodo selezionadest all'albero
#             self.tree.append(selected_node)
#             # Per ogni figlio del nodo selezionadest, calcola la distanza tra suo padre (selected_node) e il figlio
#             for node in selected_node.neighbours:
#                 child = node[0]
#                 if not child.visited:
#                     if node[1] < child.length_from_previous_node:
#                         child.length_from_previous_node = node[1]
#                         child.previous_node = selected_node.value
#         return self.tree


# # Prim con rappresentazione coda con priorità - min heap
from collections import defaultdict
import heapq


class Prim:

    def __init__(self, graph):
        self.graph = graph

    def mstPrim(self, starting_vertex):
        mst = defaultdict(set)
        visited = {starting_vertex}
        edges = [
            (cost, starting_vertex, dest)
            for dest, cost in self.graph[starting_vertex].items()
        ]

        heapq.heapify(edges)    # Trasforma edges (lista) in un heap in tempo lineare

        count = 0
        while edges:
            cost, src, dest = heapq.heappop(edges)
            if dest not in visited:
                visited.add(dest)
                mst[src].add(dest)
                count += cost
                for next_dest, cost in self.graph[dest].items():
                    if next_dest not in visited:
                        heapq.heappush(edges, (cost, dest, next_dest))
        return mst, count
