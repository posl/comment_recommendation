def bfs(G, s):
    N = len(G)
    dist = [-1]*N
    dist[s] = 0
    q = [s]
    while q:
        u = q.pop(0)
        for v in G[u]:
            if dist[v] == -1:
                dist[v] = dist[u]+1
                q.append(v)
    return dist
