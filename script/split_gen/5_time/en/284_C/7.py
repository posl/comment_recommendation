def dfs(v):
    seen[v] = True
    for i in range(1, N+1):
        if not seen[i] and G[v][i]:
            dfs(i)
N, M = map(int, input().split())
G = [[False] * (N+1) for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u][v] = G[v][u] = True
seen = [False] * (N+1)
ans = 0
for i in range(1, N+1):
    if not seen[i]:
        dfs(i)
        ans += 1
print(ans)
