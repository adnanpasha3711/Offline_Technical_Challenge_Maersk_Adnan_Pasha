import os
from graph_loader import load_graph
from dijkstra import (sp_from_source, sp_between_two_nodes, sp_to_target_node)

os.system('cls') # clear console

# Load the graph
graph, nodes = load_graph("example_graph.json")

# Define source and target
source = "A"
target = "E"

# a. Shortest path between any two nodes
print("\na. Shortest path from", source, "to", target)
result_a = sp_between_two_nodes(graph, source, target)
print(result_a)
print(f"{source} to {target}: path = {result_a[source]['path']}, time = {result_a[source]['time']}")

# b. Shortest paths to a single target from every other node
print("\nb. Shortest paths to", target, "from every other node")
result_b = sp_to_target_node(graph, target)
print(result_b)
for node in result_b:
    print(f"{node} to {target}: path = {result_b[node]['path']}, time: {result_b[node]['time']}")

# c. Shortest paths from a single source to every other node
print("\nc. Shortest paths from", source, "to every other node")
result_c = sp_from_source(graph, source)
print(result_c)
for node in result_c:
    print(f"{source} to {node}: path = {result_c[node]['path']}, time: {result_c[node]['time']}")

