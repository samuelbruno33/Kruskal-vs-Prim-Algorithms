from graph import Graph, Node
from prim import Prim
from kruskal import Kruskal
from collections import defaultdict
import random
import math


def main():
    arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O"]

    rand_graph_size = random.randint(4, 5)
    print("Size del grafo: ", rand_graph_size, "\n")

    graph = Graph()

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
            graph.addEdgeKruskal(x, y, weight)
            i += 1

    mst_kruskal = Kruskal(graph)
    mst, total_cost = mst_kruskal.mstKruskal()
    print("MST di Kruskal:")
    print(mst.printKruskalGraph())
    print("Costo totale Kruskal: ", total_cost, "\n")

    # # Prim con rappresentazione del grafo come albero
    # mst_prim = prim.Prim(graph, "A")
    # tree = mst_prim.mstPrimTree()
    # print("MST di Prim:")
    # for node in tree:
    #     print(node.printNodesPrim())
    # print("\nCosto totale Prim: ", mst_prim.calculateTotalCost())

    # # Prim con rappresentazione min heap
    i = 0
    graphConvert = []   # Converto il grafo originale in una lista con all'interno una tupla con (nodo1, nodo2, peso)
    while i < graph.edges.__len__():
        graphConvert.insert(i, list(zip(graph.edges[i].node1.printSingleNode(), graph.edges[i].node2.printSingleNode(),
                                        [graph.edges[i].weight])))
        i += 1

    g = defaultdict(dict)    # Inserisco la lista in un dizionario per renderlo leggibile alla funzione mstPrim
    for edge in graphConvert:
        first, second, weight = edge[0]
        g[first][second] = weight
    g = dict(g)

    mst_prim = Prim(g)
    print("MST di Prim:")
    mst, primCost = mst_prim.mstPrim(first)
    mst = dict(mst)
    print(mst)
    print("\nCosto totale Prim: ", primCost)


if __name__ == '__main__':
    main()
