def topsort(g, vtx):
    degree = [0] * vtx
    for node in g:
        for adjnode in g[node]:
            degree[adjnode] += 1

    bfs = [i for i in range(vtx) if degree[i] == 0]
    for node in bfs:
        for adjnode in g[node]:
            degree[adjnode] -= 1
            if degree[adjnode] == 0:
                bfs.append(adjnode)
    return bfs


from collections import defaultdict

g = defaultdict(list)
vtx, e = map(int, input().split())
for i in range(e):
    u, v = map(str, input().split())
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    g[u].append(v)
topSort = topsort(g, vtx)
topSort = [chr(i + 65) for i in topSort]
print(topSort)
"""
class Graph:

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        self.edges[node] = []

    def addEdge(self, node1, node2):
        self.edges[node1] += [node2]

    def getSub(self, node):
        return self.edges[node]

    def DFSrecu(self, start, path):

        for node in self.getSub(start):
            if node not in path:
                path = self.DFSrecu(node, path)

        if start not in path:
            path += [start]

        return path

    def topological_sort(self, start):
        topo_ordering_list = self.DFSrecu(start, [])
        # this for loop it will help you to visit all nodes in the graph if you chose arbitrary node
        # because you need to check if all nodes in the graph is visited and sort them
        for node in g.edges:
            if node not in topo_ordering_list:
                topo_ordering_list = g.DFSrecu(node, topo_ordering_list)
        return topo_ordering_list


if __name__ == "__main__":
    g = Graph()
    for node in ['A', 'B', 'C', 'D', 'E', 'F', "G", 'H', 'I', 'J', 'K', "L", 'M']:
        g.addNode(node)

    g.addEdge("A", "D")
    g.addEdge("B", "D")
    g.addEdge("C", "A")
    g.addEdge("C", "B")
    g.addEdge("D", "G")
    g.addEdge("D", "H")
    g.addEdge("E", "A")
    g.addEdge("E", "D")
    g.addEdge("E", "F")
    g.addEdge("F", "J")
    g.addEdge("F", "K")
    g.addEdge("G", "I")
    g.addEdge("H", "I")
    g.addEdge("H", "J")
    g.addEdge("I", "L")
    g.addEdge("J", "L")
    g.addEdge("J", "M")
    g.addEdge("K", "J")


    last_path1 = g.topological_sort("A")
    last_path2 = g.topological_sort("F")

    print("Start From H: ",last_path1)
    print("start From B: ",last_path2)
"""