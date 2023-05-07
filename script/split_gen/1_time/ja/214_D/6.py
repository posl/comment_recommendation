def dfs(v, p, d):
    for u, w in graph[v]:
        if u == p: continue
        d[u] = d[v] + w
        dfs(u, v, d)
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a - 1].append((b - 1, w))
    graph[b - 1].append((a - 1, w))
d = [0] * n
dfs(0, -1, d)
ans = 0
for i in range(n):
    ans += d[i]
print(ans)
