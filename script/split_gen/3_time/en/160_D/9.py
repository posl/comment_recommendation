def shortest_paths(graph, start):
    """Find shortest paths from start vertex to all other vertices of a graph
    graph is represented as a dictionary mapping vertices to iterables of
    neighbouring vertices.  start is the vertex from which to start
    shortest path search, and it is assumed to be a vertex of graph"""
    Q = set(graph) # set of all unvisited nodes
    dist = {} # dictionary of final distances
    for v in Q:
        dist[v] = float("inf") # unknown distance function from source to v
    dist[start] = 0 # distance from source to source
    while Q: # while Q is non-empty
        u = min(Q, key=dist.get) # vertex in Q with smallest distance
        Q.remove(u)
        for v in graph[u]: # where v has not yet been removed from Q.
            alt = dist[u] + 1 # length of this path
            if alt < dist[v]: # if new path is shorter
                dist[v] = alt # update distance
    return dist
