from graph import Graph, Node
from prim import Prim
from kruskal import Kruskal
from collections import defaultdict
import time
import random
import math
import matplotlib.pyplot as plt  # Import della libreria per effettuare i grafici in Python


def main():
    arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]

    # rand_graph_size = random.randint(10, 21)
    # print("Size del grafo: ", rand_graph_size, "\n")

    rand_graph_size = 3

    times = []
    times2 = []
    size = []

    plt.xlabel("No. di elementi")
    plt.ylabel("Tempo di computazione")

    while rand_graph_size <= 26:
        graph = Graph()
        graph2 = []

        size.append(rand_graph_size)

        for i in range(rand_graph_size):
            graph.addNode(Node(arr[i]))

        i = 0
        while i < rand_graph_size:
            index1 = math.floor(random.random() * rand_graph_size)
            x = arr.__getitem__(index1)
            index2 = math.floor(random.random() * rand_graph_size)
            y = arr.__getitem__(index2)
            x = x.__str__()
            y = y.__str__()
            if x == y or graph.areConnected(x, y):
                """ TODO: non fare nulla """
            else:
                weight = random.randint(1, rand_graph_size)
                graph.addEdge(x, y, weight)
                graph2.append((index1, index2, weight))
                graph2.append((index2, index1, weight))
                i += 1

        # mst_kruskal = Kruskal()
        # print("MST di Kruskal:")
        # mst1, cost = mst_kruskal.mstKruskal(graph2)
        # print(mst1)
        # print("\nCosto totale Kruskal: ", cost, "\n")

        print("----- KRUSKAL -----")
        start_time = time.process_time()
        mst_kruskal = Kruskal()
        mst_kruskal.mstKruskal(graph2)
        end_time = time.process_time() - start_time
        times.append(end_time)
        print("----------------------------\n")

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

        # mst_prim = Prim(g)
        # print("MST di Prim:")
        # mst2, primCost = mst_prim.mstPrim(first)
        # mst2 = dict(mst2)
        # print(mst2)
        # print("\nCosto totale Prim: ", primCost)

        print("----- PRIM -----")
        start_time = time.process_time()
        mst_prim = Prim(g)
        mst_prim.mstPrim(u)
        end_time = time.process_time() - start_time
        times2.append(end_time)
        print("----------------------------\n")

        rand_graph_size += 1
        print("rand_graph_size: ", rand_graph_size)

    plt.plot(size, times, marker="o", color='red')
    plt.plot(size, times2, marker="o", color='blue')
    plt.show()


if __name__ == '__main__':
    main()
