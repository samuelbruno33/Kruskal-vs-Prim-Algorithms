class Prim:

    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.tree = []  # Rappresenta l'albero prodotto
        self.vertices = self.graph.nodes

    def calculateTotalCost(self):
        total_cost = 0
        for node in self.tree:
            total_cost += node.length_from_previous_node
        return total_cost

    def mstPrim(self):
        # Inizializza la lunghezza del nodo di partenza a 0
        selected_node = self.graph.findNode(self.start)
        selected_node.length_from_previous_node = 0
        # Setta il nodo attuale selezionato come visitato
        selected_node.visited = True
        self.vertices.remove(selected_node)
        # Aggiunge il nodo selezionato all'albero
        self.tree.append(selected_node)
        # Per ogni figlio del nodo selezionato, calcola la distanza tra suo padre e il figlio
        for node in selected_node.neighbours:
            child = node[0]
            if node[1] < child.length_from_previous_node:
                child.length_from_previous_node = node[1]
                child.previous_node = selected_node.value

        while len(self.vertices) > 0:
            # Seleziona il nodo con la minima distanza dal nodo precedente
            self.vertices.sort()
            selected_node = self.vertices[0]
            selected_node.visited = True
            # Rimuove il nodo attuale dalla lista dei vertici
            self.vertices.remove(selected_node)
            # Aggiunge il nodo selezionato all'albero
            self.tree.append(selected_node)
            # Per ogni figlio del nodo selezionato, calcola la distanza tra suo padre (selected_node) e il figlio
            for node in selected_node.neighbours:
                child = node[0]
                if not child.visited:
                    if node[1] < child.length_from_previous_node:
                        child.length_from_previous_node = node[1]
                        child.previous_node = selected_node.value
        return self.tree
