from old_graph import Graph, Edge


class Kruskal:
    def __init__(self, graph):
        self.graph = graph
        # Crea un nuovo albero vuoto in forma di grafo
        self.tree = Graph()
        # Aggiunge tutti i nodi al nuovo albero
        for node in self.graph.nodes:
            self.tree.addNode(node)
        # Per ogni vertice del grafo creo un set e li salvo nella lista sets
        self.sets = [set(node.value) for node in self.graph.nodes]
        self.edges = []
        self.number_of_vertices = self.graph.numberOfNodes()
        # Ordino gli archi in base al loro peso
        self.sortEdges()
        # Rimuove gli archi dai nodi nell'albero
        for node in self.tree.nodes:
            node.neighbours.clear()

    def sortEdges(self):
        for node in self.graph.nodes:
            for edge in node.neighbours:
                self.edges.append(Edge(node, edge[0], edge[1]))
        self.edges.sort()

    def find_set(self, node):
        """
        Ritorna l'indice del rappresentante nella lista dei sets nel quale il nodo è contenuto
        """
        for index, s in enumerate(self.sets):
            if node.value in s:
                return index

    def union_set(self, set1, set2):
        """
        Unisce due rappresentanti e li elimina dalla lista
        """
        # Prendo i rappresentanti in base al loro indice nella lista
        selected_set1 = self.sets[set1]
        selected_set2 = self.sets[set2]
        # Li unisco
        new_set = selected_set1.union(selected_set2)
        # Li rimuovo
        self.sets.remove(selected_set1)
        self.sets.remove(selected_set2)
        # Aggiungo l'unione dei set nella lista
        self.sets.append(new_set)

    def mstKruskal(self):
        # Inizializzo i valori
        inserted_edges = 0
        total_cost = 0

        while True:
            # Prendo l'arco con il valore minimo
            selected_edge = self.edges.pop(0)

            set1 = self.find_set(selected_edge.node1)
            set2 = self.find_set(selected_edge.node2)

            # Se i vertici sull'arco non sono nello stesso set, allora l'arco non forma un ciclo
            # e può essere aggiunto all'albero
            if set1 != set2:
                # Aggiorno i valori
                inserted_edges += 1
                total_cost += selected_edge.weight
                self.union_set(set1, set2)
                self.tree.addEdgeKruskal(selected_edge.node1.value, selected_edge.node2.value, selected_edge.weight)
            # Controllo se il numero degli archi inseriti è uguale a |V| - 1
            if inserted_edges == self.number_of_vertices - 1:
                return self.tree, total_cost

# # IN MAIN:
# mst_kruskal = Kruskal(graph)
# mst, total_cost = mst_kruskal.mstKruskal()
# print("MST di Kruskal:")
# print(mst.printKruskalGraph())
# print("Costo totale Kruskal: ", total_cost, "\n")
