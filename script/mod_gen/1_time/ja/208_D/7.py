def dijkstra(s):
    import heapq
    d = [float("inf")] * N
    d[s] = 0
    hq = [(d[s], s)]
    while hq:
        cost, v = heapq.heappop(hq)
        if d[v] < cost:
            continue
        for nv, nc in edge[v]:
            if d[nv] > d[v] + nc:
                d[nv] = d[v] + nc
                heapq.heappush(hq, (d[nv], nv))
    return d
N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edge[a-1].append((b-1, c))
ans = 0
for i in range(N):
    d = dijkstra(i)
    for j in range(N):
        for k in range(N):
            if d[j] + d[k] <= d[i]:
                ans += d[j] + d[k]
print(ans)

if __name__ == '__main__':
    dijkstra()