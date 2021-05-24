from Edge import Edge


class Node:
    def __init__(self, _index):
        self.index = _index
        self.name = str(_index)
        self.edges = []
        self.previously_visited = None
        self.in_list = False

    def resetVisit(self):
        self.in_list = False
        self.previously_visited = None

    def addEdge(self, edge: Edge):
        self.edges.append(edge)

    def isNeighbour(self, node_index) -> bool:
        for edge in self.edges:
            if edge.destination == node_index:
                return True
        return False

    def getEdge(self, node_index) -> Edge:
        for edge in self.edges:
            if edge.destination == node_index:
                return edge

    def updateEdge(self, node_index, change):
        self.getEdge(node_index).actual_flow += change

    def __str__(self):
        return str(self.index)

    def __eq__(self, other):
        if self.index == other.index:
            return True
        return False
