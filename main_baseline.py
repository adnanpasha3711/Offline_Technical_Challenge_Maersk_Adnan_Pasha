import os
from graph_loader import load_graph
from dijkstra import (sp_from_source, 
                      sp_between_two_nodes, 
                      sp_to_target_node, 
                      sp_between_all_pairs)

os.system('cls') # clear console

# Load the graph
graph, nodes = load_graph("exercise_baseline.json")

# Define source and target
source = "cf"
target = "ec"

# a. Shortest path between any two nodes
print("\na. Shortest path from", source, "to", target)
result_a = sp_between_two_nodes(graph, source, target)
# print(result_a)
print(f"{source} to {target}: shortest_path = {result_a[source]['path']}, transit_time = {result_a[source]['time']}")

# b. Shortest paths to a single target from every other node
print("\nb. Shortest paths to", target, "from every other node")
result_b = sp_to_target_node(graph, target)
# print(result_b)
for node in result_b:
    print(f"{node} to {target}: shortest_path = {result_b[node]['path']}, transit_time: {result_b[node]['time']}")

# c. Shortest paths from a single source to every other node
print("\nc. Shortest paths from", source, "to every other node")
result_c = sp_from_source(graph, source)
# print(result_c)
for node in result_c:
    print(f"{source} to {node}: shortest_path = {result_c[node]['path']}, transit_time: {result_c[node]['time']}")

# d. Shortest paths between all pairs of nodes
print("\nc. Shortest paths between all pairs of nodes")
result_d = sp_between_all_pairs(graph)
# print(result_d)
for u in result_d:
    for v in result_d[u]:
        print(f"{u} to {v}: shortest_path = {result_d[u][v]['path']}, transit_time: {result_d[u][v]['time']}")

