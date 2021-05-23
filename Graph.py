from Node import Node
from Edge import Edge
from random import randint
import queue


class Graph:
    def __init__(self):
        self.nodes = []

    def randomGraphGenerator(self, num_of_nodes, num_of_edges, max_weight):  # digraph

        repetition_list = []
        for idx in range(num_of_nodes):
            self.nodes.append(Node(idx))
            repetition_list.append((idx, idx))

        edge_count = 0

        while edge_count < num_of_edges:
            start = randint(0, num_of_nodes - 1)
            end = randint(0, num_of_nodes - 1)
            flow = randint(1, max_weight)
            if (start, end) not in repetition_list:
                self.nodes[start].edges.append(Edge(start, end, flow))
                repetition_list.append((start, end))
                edge_count += 1

    def breadthFirstSearch(self, start, destination):  # iterative
        q = queue.Queue()
        q.put(start)
        while not q.empty():
            actual = q.get()
            if actual == destination:
                return True
            for edge in self.nodes[actual].edges:
                if edge.actual_flow > 0 and self.nodes[edge.destination].in_list == False:
                    self.nodes[edge.destination].previously_visited = actual
                    self.nodes[edge.destination].in_list = True
                    q.put(edge.destination)
        return False

    def findPath(self, start, destination):
        self.resetVisited()
        if self.breadthFirstSearch(start, destination):
            # backtracking nodes
            end = destination

            path = []
            while end != start:
                path.append(end)
                end = self.nodes[end].previously_visited

            path.append(start)
            path.reverse()
            return path
        else:
            return None

    def resetVisited(self):
        for node in self.nodes:
            node.resetVisit()

    def fordFulkersonAlgorithm(self, source, destination):
        flow = 0
        path = self.findPath(source, destination)
        while path is not None:
            print(path)
            edges = [self.nodes[first].edges[self.nodes[first].getEdgeByIndex(second)] for first, second in
                     zip(path[:-1], path[1:])]
            min_flow = min([edge.actual_flow for edge in edges])
            for edge in edges:
                edge.lowerFlow(min_flow)
            flow += min_flow
            path = self.findPath(source, destination)
            print(self)
        return flow

    def __str__(self):
        string = ""
        for node in self.nodes:
            string += f'Node {node.index} is connected to:\n'
            for edge in node.edges:
                string += f'\tnode {edge.destination} with actual flow = {edge.actual_flow}\n'

        return string
