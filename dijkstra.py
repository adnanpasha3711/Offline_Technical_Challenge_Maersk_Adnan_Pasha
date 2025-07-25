import heapq # for priority queue in dijkistra

# Shortest paths from a single source to every other node
def sp_from_source(graph, source):

    times = {node: float('inf') for node in graph} # initialize shortest times
    times[source] = 0 
    previous = {node: None for node in graph} # previous node
    priority_queue = [(0, source)] # (current time, node)
    visited = set() # initilize visited set

    # From source to all nodes
    while priority_queue:
        current_time, u = heapq.heappop(priority_queue) # extract the first node from pq
        if u in visited:
            continue # skip if already visited
        visited.add(u)
        for neighbor, weight in graph[u]: # iterate over neighbors of u
            if times[u] + weight < times[neighbor]:
                times[neighbor] = times[u] + weight
                previous[neighbor] = u
                heapq.heappush(priority_queue, (times[neighbor], neighbor)) # push updated path to pq

    # Reconstruct shortest paths
    result = {}
    for node in graph:
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        result[node] = {
            "path": path,
            "time": times[node],
        }

    return result

# Shortest path between any two nodes
def sp_between_two_nodes(graph, source, target):

    times = {node: float('inf') for node in graph} # initialize shortest times
    times[source] = 0 
    previous = {node: None for node in graph} # previous node
    priority_queue = [(0, source)] # (current time, node)
    visited = set() # initilize visited set

    while priority_queue:
        current_time, u = heapq.heappop(priority_queue) # extract the first node from pq
        if u in visited:
            continue # skip if already visited
        visited.add(u)
        if u == target:
            break # stop if target node is reached
        for neighbor, weight in graph[u]: # iterate over neighbors of u
            if times[u] + weight < times[neighbor]:
                times[neighbor] = times[u] + weight
                previous[neighbor] = u
                heapq.heappush(priority_queue, (times[neighbor], neighbor)) # push updated path to pq

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
    return result

    # Print final shortest paths and times
    print(result)
    for node in result:
        print(f"{source} to {node}: path = {result[node]['path']}, time = {result[node]['time']}")
