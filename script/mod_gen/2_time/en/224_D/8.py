def main():
    M = int(input())
    edge = [list(map(int, input().split())) for _ in range(M)]
    p = list(map(int, input().split()))
    # 0: empty, 1: piece1, 2: piece2, ..., 9: piece9
    p.insert(0, 0)
    p = [i - 1 for i in p]
    # adj[v]: vertices adjacent to v
    adj = [[] for _ in range(9)]
    for u, v in edge:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    # dist[v][i]: minimum number of operations to move piece i to vertex v
    dist = [[float("inf")] * 9 for _ in range(9)]
    for v in range(9):
        dist[v][p[v]] = 0
    # bfs
    q = []
    for v in range(9):
        q.append((v, p[v]))
    while q:
        v, i = q.pop(0)
        for u in adj[v]:
            if dist[u][i] == float("inf"):
                dist[u][i] = dist[v][i] + 1
                q.append((u, i))
    # dp[s][i]: minimum number of operations to move pieces in state s to vertices i, j, k, ..., p[s]
    dp = [[float("inf")] * 9 for _ in range(1 << 8)]
    dp[0][0] = 0
    for s in range(1 << 8):
        for v in range(9):
            for i in range(8):
                if (s >> i) & 1 == 0:
                    s2 = s | (1 << i)
                    dp[s2][p[i]] = min(dp[s2][p[i]], dp[s][v] + dist[v][i])
    ans = min(dp[-1])
    print(ans if ans != float("inf") else -1)

if __name__ == '__main__':
    main()