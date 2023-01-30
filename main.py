from graph import Graph, Node
from primHeapq import PrimHeapq
from primMinHeap import PrimMinHeap
from kruskal import Kruskal
from collections import defaultdict
import time
import random
import math
import matplotlib.pyplot as plt


def main():
    arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]

    rand_graph_size = 3

    times = []
    times2 = []
    times3 = []
    size = []

    plt.xlabel("No. di elementi")
    plt.ylabel("Tempo di computazione")

    while rand_graph_size <= arr.__len__():

        graph = Graph()
        graph2 = []
        graph3 = PrimMinHeap(rand_graph_size)

        size.append(rand_graph_size)

        for i in range(rand_graph_size):
            graph.addNode(Node(arr[i]))

        i = 0
        while i < rand_graph_size:
            index1 = math.floor(random.random() * rand_graph_size)
            x = arr.__getitem__(index1).__str__()
            index2 = math.floor(random.random() * rand_graph_size)
            y = arr.__getitem__(index2).__str__()
            if x == y or graph.areConnected(x, y):
                """ TODO: non fare nulla """
            else:
                weight = random.randint(1, rand_graph_size)
                graph.addEdge(x, y, weight)  # Per grafo di Prim con Heapq
                graph2.append((index1, index2, weight))  # Per grafo di Kruskal
                graph2.append((index2, index1, weight))  # Essendo grafo non diretto
                i += 1

        j = 0
        while j < rand_graph_size - 1:
            graph3.addToGraph(j, int(random.randint(j + 1, rand_graph_size - 1)), int(random.randint(1, 20)))
            j += 1

        # # Stampa di Kruskal
        # mst_kruskal = Kruskal()
        # print("MST di Kruskal:")
        # mst1, cost = mst_kruskal.mstKruskal(graph2)
        # print(mst1)
        # print("\nCosto totale Kruskal: ", cost, "\n")

        """----------- KRUSKAL -----------"""
        start_time = time.process_time()
        mst_kruskal = Kruskal()
        mst_kruskal.mstKruskal(graph2)
        end_time = time.process_time() - start_time
        times.append(end_time)
        """----------------------------"""

        """----------- PRIM CON MIN-HEAP-----------"""
        start_time = time.process_time()
        graph3.mstPrimMinHeap()
        end_time = time.process_time() - start_time
        times2.append(end_time)
        """----------------------------"""

        i = 0
        graphConvert = []   # Converto il grafo originale in una lista con all'interno una serie di tuple del tipo:
                            # (nodo1, nodo2, peso)
        while i < graph.edges.__len__():
            graphConvert.insert(i, list(zip(graph.edges[i].node1.value, graph.edges[i].node2.value,
                                            [graph.edges[i].weight])))
            i += 1

        g = defaultdict(dict)  # Inserisco la lista in un dizionario per renderlo leggibile alla funzione mstPrim
        for edge in graphConvert:
            u, v, weight = edge[0]
            g[u][v] = weight
        g = dict(g)

        # # Stampa di Prim
        # mst_prim = Prim()
        # print("MST di Prim:")
        # mst2, primCost = mst_prim.mstPrim(g, u)
        # mst2 = dict(mst2)
        # print(mst2)
        # print("\nCosto totale Prim: ", primCost, "\n")

        """------------ PRIM CON HEAPQ ------------"""
        start_time = time.process_time()
        mst_prim = PrimHeapq()
        mst_prim.mstPrim(g, u)
        end_time = time.process_time() - start_time
        times3.append(end_time)
        """----------------------------"""

        rand_graph_size += 1

    plt.plot(size, times, marker="o", color='red')  # In rosso Kruskal
    plt.plot(size, times2, marker="o", color='green')  # In verde Prim con min-heap
    plt.plot(size, times3, marker="o", color='blue')  # In blu Prim con Heapq
    plt.show()


if __name__ == '__main__':
    main()
