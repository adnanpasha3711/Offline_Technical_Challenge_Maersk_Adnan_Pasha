import os
from graph_loader import load_graph
from dijkstra import (sp_from_source, sp_between_two_nodes)

os.system('cls') # clear console

# Load the graph
graph, nodes = load_graph("example_graph.json")

# Define source and target
source = "A"
target = "E"

# Shortest paths from a single source to every other node
print("\nShortest paths from", source, "to all other nodes")
result_a = sp_from_source(graph, source)
print(result_a)
for node in result_a:
    print(f"{source} to {node}: path = {result_a[node]['path']}, time: {result_a[node]['time']}")

# Shortest path between any two nodes
print("\nShortest path from", source, "to", target)
result_b = sp_between_two_nodes(graph, source, target)
print(result_b)
print(f"{source} to {target}: path = {result_b[source]['path']}, time = {result_b[source]['time']}")