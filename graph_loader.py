import json

def load_graph(filename):

    # Read JSON file
    with open(filename, 'r') as f:
        data = json.load(f)

    # Extract nodes and edges
    nodes = data['nodes']
    edges = data['edges']

    # Initialize adjacency list
    graph = {node: [] for node in nodes}

    # Develop adjacency list
    for edge in edges:
        u = edge['from']
        v = edge['to']
        w = edge['transit_time']
        graph[u].append((v, w)) # add edge u-v
        graph[v].append((u, w))  # add edge v-u (bidirectional graph)

    return graph, nodes