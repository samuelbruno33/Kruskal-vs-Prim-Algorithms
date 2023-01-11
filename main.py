from graph import Graph, Node
from prim import Prim
from kruskal import Kruskal
import random
import math


def main():

    arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L", "M", "N", "O"]
    graph = Graph()

    rand_graph_size = random.randint(3, 4)
    print("Size del grafo: ", rand_graph_size, "\n")

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
            i += 1

    mst_kruskal = Kruskal(graph)
    mst, total_cost = mst_kruskal.mstKruskal()
    print("MST di Kruskal:")
    print(mst.printKruskalGraph())
    print("Costo totale Kruskal: ", total_cost)

    print("\n")

    mst_prim = Prim(graph, "A")
    tree = mst_prim.mstPrim()
    print("MST di Prim:")
    for node in tree:
        print(node.printNodesPrim())
    print("\nCosto totale Prim: ", mst_prim.calculateTotalCost())


if __name__ == '__main__':
    main()
