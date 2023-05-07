def solve():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    adj = [[] for _ in range(N)]
    for u, v in edges:
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    ans = 0
    for i in range(M):
        u, v = edges[i]
        u -= 1
        v -= 1
        for a in adj[u]:
            if a == v:
                continue
            for b in adj[v]:
                if b == u:
                    continue
                if a in adj[b]:
                    continue
                ans += 1
    print(ans // 6)
    return
