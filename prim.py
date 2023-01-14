# # Prim con rappresentazione coda con priorità - min heap
from collections import defaultdict
import heapq


class Prim:

    def __init__(self, graph):
        self.graph = graph

    def mstPrim(self, starting_vertex):
        mst = defaultdict(set)
        visited = {starting_vertex}
        graph_edges = [
            (cost, starting_vertex, dest)
            for dest, cost in self.graph[starting_vertex].items()
        ]

        heapq.heapify(graph_edges)    # Trasforma graph_edges (lista) in un heap in tempo lineare

        count = 0
        while graph_edges:
            cost, src, dest = heapq.heappop(graph_edges)
            if dest not in visited:
                visited.add(dest)
                mst[src].add(dest)
                count += cost
                for next_dest, cost in self.graph[dest].items():
                    if next_dest not in visited:
                        heapq.heappush(graph_edges, (cost, dest, next_dest))
        return mst, count
