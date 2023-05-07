def dijkstra(N, G, s):
    # 1-indexed
    # N: 頂点数
    # G: 隣接リスト
    # s: 始点
    d = [float('inf')]*(N+1)
    d[s] = 0
    used = [False]*(N+1)
    used[s] = True
    edgelist = []
    for e in G[s]:
        heapq.heappush(edgelist, e)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = True
        for e in G[v]:
            if used[e[1]]:
                continue
            heapq.heappush(edgelist, [e[0]+d[v], e[1]])
    return d

if __name__ == '__main__':
    dijkstra()