import math


class Node:
    def __init__(self, value, neighbours=None):
        self.value = value
        if neighbours is None:
            self.neighbours = []
        else:
            self.neighbours = neighbours
        self.length_from_previous_node = math.inf   # Inizializzo ad infinito
        self.previous_node = None
        self.visited = False

    def hasNeighbours(self):
        if len(self.neighbours) == 0:
            return False
        return True

    # def numberOfNeighbours(self):
    #     return len(self.neighbours)

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def __eq__(self, other):
        """
            Determina l'equivalenza tra due nodi (equal)
            ---------------------------------------------
            Override dell'operazione di base, mi serve per l'operazione di sort dei vertici nel calcolo del mst di Prim
        """
        return self.value == other.value

    def __gt__(self, other):
        """
            Determina quale nodo è più grande (greater)
            --------------------------------------------
            Override dell'operazione di base, mi serve per l'operazione di sort dei vertici nel calcolo del mst di Prim
        """
        return self.length_from_previous_node > other.length_from_previous_node

    def printNodesPrim(self):
        return f"{self.previous_node} -> {self.value}"

    def printNodesKruskal(self):
        returned_string = ""
        if self.hasNeighbours():
            for neighbour in self.neighbours:
                returned_string += f"{self.value} -> {neighbour[0].value} "
        else:
            returned_string += f"{self.value} -> None"
        return returned_string


class Graph:
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes

    def addNode(self, node):
        self.nodes.append(node)

    def findNode(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def addEdge(self, value1, value2, weight=1):
        node1 = self.findNode(value1)
        node2 = self.findNode(value2)

        if (node1 is not None) and (node2 is not None):
            node1.addNeighbour((node2, weight))
            node2.addNeighbour((node1, weight))
        else:
            raise Exception("Errore: uno o più nodi non trovati!")

    # def numberOfNodes(self):
    #     return len(self.nodes)

    def areConnected(self, node1, node2):
        first = self.findNode(node1)
        second = self.findNode(node2)

        for neighbour in first.neighbours:
            if neighbour[0].value == second.value:
                return True
        return False

    def printKruskalGraph(self):
        graph = ""
        for node in self.nodes:
            graph += f"{node.printNodesKruskal()}\n"
        return graph
