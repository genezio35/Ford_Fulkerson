from typing import List
from Node import Node
from Edge import Edge
from random import randint
import queue
import json

def minimumFlow(edges: List[Edge]):
    return min([edge.actual_flow for edge in edges])


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
                self.nodes[start].addEdge(Edge(start, end, flow))
                repetition_list.append((start, end))
                edge_count += 1

    def fromArray(self, array):

        for idx, node_arr in enumerate(array):
            node = Node(idx)
            for edge in node_arr:
                node.addEdge(Edge(idx, edge[0], edge[1]))
            self.nodes.append(node)

    def fromJSON(self, file):
        self.fromArray(json.load(file))


    def wikiGraph(self):  # test for wikipedia example (ans = 5)
        self.nodes = [Node(idx) for idx in range(7)]
        self.nodes[0].addEdge(Edge(0, 1, 3))
        self.nodes[0].addEdge(Edge(0, 3, 3))

        self.nodes[1].addEdge(Edge(1, 2, 4))

        self.nodes[2].addEdge(Edge(2, 0, 3))
        self.nodes[2].addEdge(Edge(2, 3, 1))
        self.nodes[2].addEdge(Edge(2, 4, 2))

        self.nodes[3].addEdge(Edge(3, 4, 2))
        self.nodes[3].addEdge(Edge(3, 5, 6))

        self.nodes[4].addEdge(Edge(4, 1, 1))
        self.nodes[4].addEdge(Edge(4, 6, 1))

        self.nodes[5].addEdge(Edge(5, 6, 9))

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

    def pathToEdges(self, path: List[int]):
        return [self.nodes[first].getEdge(second) for first, second in zip(path[:-1], path[1:])]

    def fordFulkersonAlgorithm(self, source, destination):
        flow = 0
        path = self.findPath(source, destination)
        while path is not None:
            edges = self.pathToEdges(path)
            min_flow = minimumFlow(edges)
            flow += min_flow
            for edge in edges:
                edge.lowerFlow(min_flow)
                if not self.nodes[edge.destination].isNeighbour(edge.source):
                    self.nodes[edge.destination].addEdge(Edge(edge.destination, edge.source, min_flow))
                else:
                    self.nodes[edge.destination].updateEdge(edge.source, min_flow)

            path = self.findPath(source, destination)
        return flow

    def toList(self):
        return [[[edge.destination, edge.flow] for edge in node.edges] for node in self.nodes]

    def toJSON(self, name):
        with open(name, 'w') as file:
            json.dump(self.toList(), file)

    def __str__(self):
        string = ""
        for node in self.nodes:
            string += f'Node {node.index} is connected to:\n'
            for edge in node.edges:
                string += f'\tnode {edge.destination} with actual flow = {edge.actual_flow}\n'

        return string
