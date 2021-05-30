# Ford_Fulkerson
# Ford-Fulkerson's method of finding the maximum flow.

This program searches for the maximum flow of the graph.

## How to run code:

1) To run this code download zip, or clone this repository using git:
```python
git clone https://github.com/genezio35/Ford_Fulkerson.git
```

2) Then go to project directory and run the main.py
```python
python3 main.py
```
3) Follow instructions given in console/terminal. Write the name of .json adjacency list file and You'll be presented with results.

# Adjacency list

The adjacency list structure - .json file - looks like this: 
```
[ [ [vertex, weight], [vertex, weight], [vertex, weight], ... ],
  [ [ [vertex, weight], [vertex, weight], [vertex, weight], ... ] ],
  .
  .
  [ [vertex, weight], [vertex, weight], ... ]
  ]
```
Every line represents a node, starting from 0. In brackets for nth node, 
there are indexes of nodes that are connected to this node.
If there is no edges starting at a node, we simply leave "[]" brackets. As a second number
in [vertex, flow] bracket we pass flow.

You can use already created .json files or create new. Put them in /Example_graphs directory.

Example:
```python
[[[1, 3], [3, 3]],
  [[2, 4]],
  [[0, 3], [3, 1], [4, 2]],
  [[4, 2], [5, 6]],
  [[1, 1], [6, 1]],
  [[6, 9]],
  []
]
```

# How program return answer
```
At the end of working, the program prints the maximum flow of graph, for example:
```python
Max flow of the graph from node 0 to node 10 is equal to 15 
```
