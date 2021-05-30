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
there are nodes that are connected to this nth node, where - because graph is oriented -
edges are "coming out" of this nth node and poiniting to all nodes in brackets. 
If there is no edges starting at a node, we simply leave "[]" brackets. Also at second position
in [vertex, weight] bracket we pass weight.

You can use already created .json files or create new ones. Make sure You put them in /adjacency_lists directory
where the examples are.

Example:
```python
[[ [1,5], [2,10], [3,5]], #0th node, 0->1, 0->2, 0->3 with weights, in order, 5, 10, 5.
  [[4,10]], #1st node, 1->4 with weight 10
  [[1,15], [5,20]],
  [[5,20]],
  [[5,25], [7,10]],
  [[3,5], [8,30]],
  [[8,5], [9,10]],
  [[10,5]],
  [[10,15], [9,5], [4,15]],
  [[10,10]],
  [] #10th node, no edges starting at this node so : [].
]
```

# How program return answer
```
At the end of working, the program prints the maximum flow of graph, for example:
```python
Max flow of the graph from node 0 to node 10 is equal to 15 
```
