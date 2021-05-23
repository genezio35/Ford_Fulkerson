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

    def getEdgeByIndex(self, neighbour):
        for idx, edge in enumerate(self.edges):
            if edge.destination == neighbour:
                return idx

    def __str__(self):
        return str(self.index)

    def __eq__(self, other):
        if self.index == other.index:
            return True
        return False

