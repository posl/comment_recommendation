def dijkstra(edges, num_v):
    dist = [float("inf")] * num_v
    dist[0] = 0
    prev = [-1] * num_v
    q = []
    heapq.heappush(q, (0, 0))
    while len(q) > 0:
        _, u = heapq.heappop(q)
        for v, c in edges[u]:
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                prev[v] = u
                heapq.heappush(q, (dist[v], v))
    return dist, prev
