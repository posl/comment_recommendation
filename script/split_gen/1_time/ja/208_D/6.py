def dijkstra(s, N, graph):
    import heapq
    INF = 10**18
    dist = [INF]*N
    dist[s] = 0
    que = [(0, s)]
    while que:
        d, v = heapq.heappop(que)
        if dist[v] < d:
            continue
        for e, cost in graph[v]:
            if dist[e] > dist[v] + cost:
                dist[e] = dist[v] + cost
                heapq.heappush(que, (dist[e], e))
    return dist
