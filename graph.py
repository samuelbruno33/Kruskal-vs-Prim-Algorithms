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

    # def hasNeighbours(self):
    #     if len(self.neighbours) == 0:
    #         return False
    #     return True
    #
    # def numberOfNeighbours(self):
    #     return len(self.neighbours)

    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def __eq__(self, other):
        """
            Determines if two nodes are equal or not, checking their values
            Parameters
            ----------
                other: Node:
                    Represent the other node with which the current node is compared
            Returns
            -------
                Boolean
        """
        return self.value == other.value

    def __gt__(self, other):
        """
            Determines which of the two nodes are greater than the other,
            comparing the length from the previous node for each of them.
            Parameters
            ----------
                other: Node:
                    Represent the other node with which the current node is compared
            Returns
            -------
                Boolean
        """
        return self.length_from_previous_node > other.length_from_previous_node

    def printPreviousAndCurrentNode(self):
        return f"{self.previous_node} -> {self.value}"

    # def __eq__(self, other):
    #     if isinstance(other, Node):
    #         return self.value == other.value
    #     return self.value == other
    #
    # def __str__(self):
    #     returned_string = ""
    #     if self.has_neighbors():
    #         for neighboor in self.neighbors:
    #             returned_string += f"{self.value} -> {neighboor[0].value} "
    #     else:
    #         returned_string += f"{self.value} -> None"
    #
    #     return returned_string


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

    # def areConnected(self, node1, node2):
    #     node1 = self.findNode(node1)
    #     node2 = self.findNode(node2)
    #
    #     for neighbour in node1.neighbours:
    #         if neighbour[0].value == node2.value:
    #             return True
    #     return False

    # def printAll(self):
    #     graph = ""
    #     for node in self.nodes:
    #         graph += f"{node.printPreviousAndCurrentNode()}\n"
    #     return graph
