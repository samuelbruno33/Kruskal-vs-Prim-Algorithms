from graph import Graph, Node
from prim import Prim


def main():
    prim = Graph()
    
    prim.addNode(Node('A'))
    prim.addNode(Node('B'))
    prim.addNode(Node('C'))
    prim.addNode(Node('D'))
    prim.addNode(Node('E'))
    prim.addNode(Node('F'))
    prim.addNode(Node('G'))
    prim.addNode(Node('H'))
    prim.addNode(Node('I'))
    
    prim.addEdge('A', 'B', 9)
    prim.addEdge('A', 'C', 4)
    prim.addEdge('B', 'C', 2)
    prim.addEdge('B', 'D', 1)
    prim.addEdge('B', 'E', 7)
    prim.addEdge('C', 'D', 4)
    prim.addEdge('C', 'F', 3)
    prim.addEdge('D', 'E', 2)
    prim.addEdge('D', 'F', 5)
    prim.addEdge('E', 'F', 6)
    prim.addEdge('E', 'G', 3)
    prim.addEdge('F', 'G', 8)
    prim.addEdge('F', 'H', 5)
    prim.addEdge('G', 'H', 1)
    prim.addEdge('G', 'I', 3)
    prim.addEdge('H', 'I', 2)

    mst_prim = Prim(prim, "A")
    tree = mst_prim.mst_prim()
    total_cost = mst_prim.calculateTotalCost()
    print("MST di Prim")
    for node in tree:
        print(node.printPreviousAndCurrentNode())
    print("Costo totale Prim: ", total_cost)


if __name__ == '__main__':
    main()

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
# Total Cost: 18
