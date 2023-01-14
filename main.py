# from old_kruskal import Kruskal
# from old_graph import Graph, Node
from graph import Graph, Node
from prim import Prim
from collections import defaultdict
import random
import math


def main():
    arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "Z"]

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
            print("x: ", x)
            print("y: ", y)
            print("weight: ", weight)
            graph.addEdgeKruskal(x, y, weight)
            i += 1

    i = 0
    graphConvert = []   # Converto il grafo originale in una lista con all'interno una tupla con (nodo1, nodo2, peso)
    while i < graph.edges.__len__():
        graphConvert.insert(i, list(zip(graph.edges[i].node1.value, graph.edges[i].node2.value,
                                        [graph.edges[i].weight])))
        i += 1

    print(graphConvert)

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
