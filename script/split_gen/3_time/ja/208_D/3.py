def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, c))
        G[b].append((a, c))
    INF = 10**10
    ans = 0
    for k in range(N):
        dist = [INF for _ in range(N)]
        dist[k] = 0
        que = [(0, k)]
        while que:
            d, v = heapq.heappop(que)
            if dist[v] < d:
                continue
            for nv, nd in G[v]:
                if dist[nv] > d + nd:
                    dist[nv] = d + nd
                    heapq.heappush(que, (dist[nv], nv))
        for i in range(N):
            if i == k:
                continue
            ans += dist[i]
    print(ans)
