# # Prim con rappresentazione coda con priorità - min heap
from collections import defaultdict
import heapq


class Prim:

    def __init__(self, graph):
        self.graph = graph

    def mstPrim(self, starting_vertex):
        mst = defaultdict(set)
        visited = {starting_vertex}     # Creo un set di nodi visitati
        # graph_edges = []
        # for cost, dest in self.graph[starting_vertex].items():
        #     graph_edges.append((cost, starting_vertex, dest))
        graph_edges = [
            (cost, starting_vertex, dest)
            for cost, dest in self.graph[starting_vertex].items()  # Creo una List Comprehension con all'interno gli archi del grafo
        ]

        heapq.heapify(graph_edges)    # Trasforma graph_edges (lista) in un heap in tempo lineare

        count = 0
        while graph_edges:
            cost, src, dest = heapq.heappop(graph_edges)    # Rimuove e prende il min-heap della lista
            if dest not in visited:
                visited.add(dest)
                mst[src].add(dest)
                count += cost
                for next_dest, cost in self.graph[dest].items():
                    if next_dest not in visited:
                        heapq.heappush(graph_edges, (cost, dest, next_dest))
        return mst, count
