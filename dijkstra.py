import os
import json
import heapq # for priority queue in dijkistra

os.system('cls') # clear console

# Read JSON file
with open("example_graph.json", 'r') as f:
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

# Print results    
print(graph)
for u in graph:
    print(f"{u}: {graph[u]}")


# Dijkistra algorithm
source = "A"
target = "E"
times = {node: float('inf') for node in graph} # initialize shortest times
times[source] = 0 
previous = {node: None for node in graph} # previous node
priority_queue = [(0, source)] # (current time, node)
visited = set() # initilize visited set

# # From source to all nodes
# while priority_queue:
#     current_time, u = heapq.heappop(priority_queue) # extract the first node from pq
#     if u in visited:
#         continue # skip if already visited
#     visited.add(u)
#     for neighbor, weight in graph[u]: # iterate over neighbors of u
#         if times[u] + weight < times[neighbor]:
#             old_time = times[neighbor]
#             times[neighbor] = times[u] + weight
#             previous[neighbor] = u
#             heapq.heappush(priority_queue, (times[neighbor], neighbor)) # push updated path to pq
#             print(f"Updated time for {neighbor}: {old_time} to {times[neighbor]}")
#         else:
#             print(f"No update required for {neighbor}")

# # Reconstruct shortest paths
# result = {}
# for node in graph:
#     path = []
#     current = node
#     while current is not None:
#         path.append(current)
#         current = previous[current]
#     path.reverse()
#     result[node] = {
#         "path": path,
#         "time": times[node],
#     }

# Between 2 nodes
while priority_queue:
    current_time, u = heapq.heappop(priority_queue) # extract the first node from pq
    if u in visited:
        continue # skip if already visited
    visited.add(u)
    if u == target:
        break
    for neighbor, weight in graph[u]: # iterate over neighbors of u
        if times[u] + weight < times[neighbor]:
            old_time = times[neighbor]
            times[neighbor] = times[u] + weight
            previous[neighbor] = u
            heapq.heappush(priority_queue, (times[neighbor], neighbor)) # push updated path to pq
            print(f"Updated time for {neighbor}: {old_time} to {times[neighbor]}")
        else:
            print(f"No update required for {neighbor}")

# Reconstruct shortest paths
result = {}
path = []
current = target
while current is not None:
    path.append(current)
    current = previous[current]
path.reverse()
result[source] = {
    "path": path,
    "time": times[target],
}

# Print final shortest paths and times
print(result)
for node in result:
    print(f"{source} to {node}: path = {result[node]['path']}, time = {result[node]['time']}")
