from graph import Graph, Node
from prim import Prim
from kruskal import Kruskal


def main():
    graph1 = Graph()
    
    graph1.addNode(Node('A'))
    graph1.addNode(Node('B'))
    graph1.addNode(Node('C'))
    graph1.addNode(Node('D'))
    graph1.addNode(Node('E'))
    graph1.addNode(Node('F'))
    graph1.addNode(Node('G'))
    graph1.addNode(Node('H'))
    graph1.addNode(Node('I'))
    
    graph1.addEdge('A', 'B', 9)
    graph1.addEdge('A', 'C', 4)
    graph1.addEdge('B', 'C', 2)
    graph1.addEdge('B', 'D', 1)
    graph1.addEdge('B', 'E', 7)
    graph1.addEdge('C', 'D', 4)
    graph1.addEdge('C', 'F', 3)
    graph1.addEdge('D', 'E', 2)
    graph1.addEdge('D', 'F', 5)
    graph1.addEdge('E', 'F', 6)
    graph1.addEdge('E', 'G', 3)
    graph1.addEdge('F', 'G', 8)
    graph1.addEdge('F', 'H', 5)
    graph1.addEdge('G', 'H', 1)
    graph1.addEdge('G', 'I', 3)
    graph1.addEdge('H', 'I', 2)

    mst_prim = Prim(graph1, "A")
    tree = mst_prim.mstPrim()
    print("MST di Prim:")
    for node in tree:
        print(node.printNodesPrim())

    print("\nCosto totale Prim: ", mst_prim.calculateTotalCost())
    print("\n")
    graph2 = Graph()

    graph2.addNode(Node('A'))
    graph2.addNode(Node('B'))
    graph2.addNode(Node('C'))
    graph2.addNode(Node('D'))
    graph2.addNode(Node('E'))
    graph2.addNode(Node('F'))
    graph2.addNode(Node('G'))
    graph2.addNode(Node('H'))
    graph2.addNode(Node('I'))

    graph2.addEdge('A', 'B', 9)
    graph2.addEdge('A', 'C', 4)
    graph2.addEdge('B', 'C', 2)
    graph2.addEdge('B', 'D', 1)
    graph2.addEdge('B', 'E', 7)
    graph2.addEdge('C', 'D', 4)
    graph2.addEdge('C', 'F', 3)
    graph2.addEdge('D', 'E', 2)
    graph2.addEdge('D', 'F', 5)
    graph2.addEdge('E', 'F', 6)
    graph2.addEdge('E', 'G', 3)
    graph2.addEdge('F', 'G', 8)
    graph2.addEdge('F', 'H', 5)
    graph2.addEdge('G', 'H', 1)
    graph2.addEdge('G', 'I', 3)
    graph2.addEdge('H', 'I', 2)

    mst_kruskal = Kruskal(graph2)
    mst, total_cost = mst_kruskal.mstKruskal()
    print("MST di Kruskal:")
    print(mst.printKruskalGraph())
    print("Costo totale Kruskal: ", total_cost)


if __name__ == '__main__':
    main()
    
# MST di Kruskal
# A -> C
# B -> D B -> C
# C -> F
# D -> E
# E -> G
# F -> None
# G -> H
# H -> I
# I -> None
# Costo totale Kruskal: 18


# MST di Prim
# None -> A
# A -> C
# C -> B
# B -> D
# D -> E
# C -> F
# E -> G
# G -> H
# H -> I
# Costo totale Prim: 18
