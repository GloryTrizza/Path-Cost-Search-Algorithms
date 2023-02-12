# Path-Cost-Search-Algorithms

## Overview
The code implements various search algorithms to find all possible paths, the shortest path and the cheapest path in a graph. The graph is represented as a dictionary where each vertex is a key and its corresponding set of neighbors is the value. The cost of moving from one vertex to another is also defined in the code.

## Classes and Methods
Class Environment: defines the graph structure, cost of moving from one vertex to another and the start and goal vertices.
Class Agent: inherits from Environment and implements the following algorithms:
Depth First Search (DFS)
Breadth First Search (BFS)
Uniform Cost Search (UCS)
The DFS method uses a stack to keep track of vertices to be visited. It starts at the start vertex and adds all its neighbors to the stack, and continues visiting vertices until the goal is reached or the stack is empty. The method returns the longest path from the start to the goal.

The BFS method uses a queue to keep track of vertices to be visited. It starts at the start vertex and adds all its neighbors to the queue, and continues visiting vertices until the goal is reached or the queue is empty. The method returns the shortest path from the start to the goal.

The UCS method uses a priority queue to keep track of vertices to be visited based on their costs. It starts at the start vertex, adds all its neighbors to the queue with their corresponding costs and continues visiting vertices until the goal is reached or the queue is empty. The method returns the cheapest path from the start to the goal.

The get_cost method calculates the cost of a given path by summing the cost of moving from one vertex to another.

The __init__ method creates an instance of the Environment class and calls the DFS, BFS, and UCS methods to find all possible paths, the shortest path, and the cheapest path respectively.

## Usage
Define the graph structure, cost of moving from one vertex to another, and the start and goal vertices in the Environment class.
Create an instance of the Environment class.
Create an instance of the Agent class and pass the Environment instance as an argument.
The output of the code will show the longest path found by DFS, the shortest path found by BFS, and the cheapest path found by UCS.



