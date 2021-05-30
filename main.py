from Graph import Graph
import json

if __name__ == "__main__":
    _end = False
    path = 'Example_graphs/'
    while not _end:
        print("To run program write the name of the graph's adjacency list in format \"graphName.json\".")
        try:
            source = input("json file-name: ")
            graph = Graph()
            graph.fromJSON(open(path + source))
            print("File loaded successfully!\n", graph)

        except:
            try:
                print("Can't find that file in 'Example_graphs' folder. Try again:")
                source = input("json file-name: ")
                graph = Graph()
                graph.fromJSON(open(path + source))
                print("File loaded successfully!\n", graph)
            except:
                print("Incorrect file_name")
        try:
            start = input("Type source node index (starting from 0): ")
            end = input("Type destination node indexes (starting from 0): ")
            start = int(start)
            end = int(end)
            print("Max flow of the graph from node ", start, " to node ", end, " is equal to ",
                  graph.fordFulkersonAlgorithm(start, end))
        except:
            print("Wrong node indexes. Try again")
            start = input("Type source node index (starting from 0): ")
            end = input("Type destination node indexes (starting from 0): ")
            start = int(start)
            end = int(end)
            print("Max flow of the graph from node ", start, " to node ", end, " is equal to ",
                  graph.fordFulkersonAlgorithm(start, end))
        answer = ""
        while answer != "No" or answer != "Yes":
            answer = input("Do You wish to input another graph?(Yes/No): ")
            if answer == "Yes":
                break
            elif answer == "No":
                _end = True
                break
