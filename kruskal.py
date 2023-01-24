class UnionFind:
    def __init__(self, n):
        self.parents = {i: i for i in range(0, n)}  # set che rappresenta un puntatore/indice al padre di un nodo
        self.groups = n     # Rappresenta la dimensione della collezione

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        self.parents[y] = x
        self.groups -= 1
        return True


class Kruskal:

    def __init__(self):
        pass

    def mstKruskal(self, graph):
        n = len(graph)
        edges = []
        for i in graph:
            edges.append((i[2], i[0], i[1]))    # Inserisco nella lista degli archi: peso, nodo1, nodo2

        edges.sort()    # Ordino la lista di archi

        cost = 0
        mst = []
        union_find = UnionFind(n)
        for weight, u, v in edges:
            if union_find.find(u) != union_find.find(v):    # Se non sono nello stess Set allora non formano un ciclo
                union_find.union(u, v)      # Unisco i due Set in un unico solo
                mst.append((u, v))   # Inserisco in lista di mst
                cost += weight     # Conto costo totale mst
        return mst, cost
