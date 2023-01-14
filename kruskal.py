class DisjointSet:
    def __init__(self, n):
        self.parents = {i: i for i in range(0, n)}
        self.groups = n

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
    def mstKruskal(self, points):
        n = len(points)
        edges = []
        for i in points:
            edges.append((i[2], i[0], i[1]))
            
        edges.sort()

        cost = 0
        g = []
        union_find = DisjointSet(n)
        for weight, u, v in edges:
            if union_find.find(u) != union_find.find(v):
                union_find.union(u, v)
                g.append((u, v))
                cost += weight
        return g, cost
