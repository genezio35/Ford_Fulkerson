from Graph import Graph

g = Graph()
g.randomGraphGenerator(5, 13, 5)
print(g)
print(g.fordFulkersonAlgorithm(0, 4))
