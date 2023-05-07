def dijkstra(n, s, edges):
    import heapq
    from collections import defaultdict
    g = defaultdict(list)
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))
    dist = [float('inf')] * n
    dist[s] = 0
    que = [(0, s)]
    while que:
        d, v = heapq.heappop(que)
        if d > dist[v]:
            continue
        for nv, w in g[v]:
            if dist[nv] > d + w:
                dist[nv] = d + w
                heapq.heappush(que, (d + w, nv))
    return dist

if __name__ == '__main__':
    dijkstra()