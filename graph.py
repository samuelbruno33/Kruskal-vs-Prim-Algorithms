class Node:
    def __init__(self, value, neighbours=None):
        self.value = value
        if neighbours is None:
            self.neighbours = []
        else:
            self.neighbours = neighbours
            
    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes
        self.edges = []

    def addNode(self, node):
        self.nodes.append(node)

    def findNode(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None
    
    def areConnected(self, node1, node2):
        u = self.findNode(node1)
        v = self.findNode(node2)

        for neighbour in u.neighbours:      # Controllo se nei vicini del primo nodo sia presente il seconod nodo
            if neighbour[0].value == v.value:
                return True
        return False

    def addEdge(self, value1, value2, weight=1):
        node1 = self.findNode(value1)
        node2 = self.findNode(value2)

        if (node1 is not None) and (node2 is not None):
            node1.addNeighbour((node2, weight))     # Nodi di controllo per check di inserimento nel grafo
            node2.addNeighbour((node1, weight))
            self.edges.append(Edge(node1, node2, weight))  # Aggiungo archi per convertire lista in dizionario per Prim (graphConvert)
            self.edges.append(Edge(node2, node1, weight))  # Essendo grafo non diretto
        else:
            raise Exception("Errore: uno o più nodi non trovati!")
