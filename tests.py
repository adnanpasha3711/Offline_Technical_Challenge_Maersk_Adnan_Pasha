import os
from graph_loader import load_graph
from dijkstra import (sp_from_source, 
                      sp_between_two_nodes, 
                      sp_to_target_node, 
                      sp_between_all_pairs)

os.system('cls') # clear console

def test(filename, source, target):
    graph, nodes = load_graph(filename)
    print(f"{filename}")
    print(f"Source: {source}, Target: {target}")

    # a. Shortest path between any two nodes
    result_a = sp_between_two_nodes(graph, source, target)
    print(f"a. {source} to {target}: shortest_path = {result_a[source]['path']}, transit_time = {result_a[source]['time']}")

    # b. Shortest paths to a single target from every other node
    result_b = sp_to_target_node(graph, target)
    for node in result_b:
        print(f"b. {node} to {target}: shortest_path = {result_b[node]['path']}, transit_time = {result_b[node]['time']}")

    # c. Shortest paths from a single source to every other node
    result_c = sp_from_source(graph, source)
    for node in result_c:
        print(f"c. {source} to {node}: shortest_path = {result_c[node]['path']}, transit_time = {result_c[node]['time']}")

    # d. Shortest paths between all pairs of nodes
    result_d = sp_between_all_pairs(graph)
    for u in result_d:
        for v in result_d[u]:
            print(f"d. {u} to {v}: shortest_path = {result_d[u][v]['path']}, transit_time = {result_d[u][v]['time']}")

# Run dijkstra on test graphs
test("test_graph_triangle.json", "A", "C")
test("test_graph_square.json", "D", "F")
test("test_graph_5nodes.json", "H", "L")