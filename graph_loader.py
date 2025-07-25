import json

# Import from JSON file and create adjacency list
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

# Export shortest paths to JSON file in given format
def write_results(results, filename, mode, source=None, target=None):

    routes = []

    if mode == "sp_between_two_nodes":
        data = results[source]
        routes.append({
            "from": source,
            "to": target,
            "path": data["path"],
            "transit_time": data["time"]
        })

    elif mode == "sp_to_target_node":
        for node, data in results.items():
            routes.append({
                "from": node,
                "to": target,
                "path": data["path"],
                "transit_time": data["time"]
            })

    elif mode == "sp_from_source":
        for node, data in results.items():
            routes.append({
                "from": source,
                "to": node,
                "path": data["path"],
                "transit_time": data["time"]
            })

    elif mode == "sp_between_all_pairs":
        for from_node in results:
            for to_node in results[from_node]:
                data = results[from_node][to_node]
                routes.append({
                    "from": from_node,
                    "to": to_node,
                    "path": data["path"],
                    "transit_time": data["time"]
                })

    with open(filename, 'w') as f:
        json.dump({"routes": routes}, f, indent=2)
    print(f"JSON output file: {filename}")
