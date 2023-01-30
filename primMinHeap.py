import math
from collections import defaultdict


class Heap:

    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []   # Posizione di un vertice nell'heap

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def minHeapify(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left

        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right
            
        if smallest != index:
            self.pos[self.array[smallest][0]] = index
            self.pos[self.array[index][0]] = smallest
            self.swapMinHeapNode(smallest, index)
            self.minHeapify(smallest)

    def extractMin(self):
        if self.isEmpty():
            return

        root = self.array[0]
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
        
        self.size -= 1
        self.minHeapify(0)
        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):
        i = self.pos[v]
        self.array[i][1] = dist

        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]:
            self.pos[self.array[i][0]] = (i - 1) / 2
            self.pos[self.array[(i - 1) // 2][0]] = i
            self.swapMinHeapNode(i, (i - 1) // 2)

            i = (i - 1) // 2
            
    def isInMinHeap(self, v):
        if self.pos[v] < self.size:
            return True
        return False


class PrimMinHeap:

    def __init__(self, nodes):
        self.graph = defaultdict(list)
        self.V = nodes  # Numero di vertici nel grafo

    def addToGraph(self, src, dest, weight):
        new_node = [dest, weight]
        self.graph[src].append(new_node)

        new_node = [src, weight]
        self.graph[dest].append(new_node)

    def mstPrimMinHeap(self):
        key = []
        parent = []
        minHeap = Heap()

        for v in range(self.V):
            parent.append(-700)
            key.append(math.inf)
            minHeap.array.append(minHeap.newMinHeapNode(v, key[v]))
            minHeap.pos.append(v)

        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0])

        minHeap.size = self.V

        while not minHeap.isEmpty():
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            for i in self.graph[u]:

                v = i[0]
                if minHeap.isInMinHeap(v) and i[1] < key[v]:
                    key[v] = i[1]
                    parent[v] = u
                    minHeap.decreaseKey(v, key[v])

        self.printAll(parent, self.V, key)

    def printAll(self, parent, n, key, count=0):
        for i in range(1, n):
            print("%d - %d" % (parent[i], i))
            count += key[i]
        print("\nCosto totale Prim: ", count, "\n")
