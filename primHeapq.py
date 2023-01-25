from collections import defaultdict
import heapq


class PrimHeapq:

    def __init__(self):
        pass

    def mstPrim(self, graph, starting_node):
        mst = defaultdict(set)
        visited = {starting_node}     # Creo un set di nodi visitati
        graph_edges = []
        for v, cost in graph[starting_node].items():
            graph_edges.append((cost, starting_node, v))   # Inserisco nella lista degli archi del grafo

        heapq.heapify(graph_edges)    # Trasforma graph_edges in un heap in tempo lineare

        count = 0
        while graph_edges:
            cost, u, v = heapq.heappop(graph_edges)    # Fa il pop, quindi rimuove e prende il min-heap della lista
            if v not in visited:
                visited.add(v)
                mst[u].add(v)   # Aggiungo v come collegamento di u nel set mst
                count += cost   # Conto costo totale mst
                for next_node, cost in graph[v].items():    # Controllo successivamente tutti i nodi collegati
                    if next_node not in visited:
                        heapq.heappush(graph_edges, (cost, v, next_node))   # Fa il push, quindi inserisce la tupla
                        # nell'heap se uno dei nodi successivi collegati non è presente nei nodi visitati
        return mst, count
