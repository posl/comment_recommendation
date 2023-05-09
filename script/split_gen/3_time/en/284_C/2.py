def dfs(v, visited, g):
    visited[v] = True
    for i in g[v]:
        if not visited[i]:
            dfs(i, visited, g)
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
visited = [False] * n
ans = 0
for i in range(n):
    if not visited[i]:
        dfs(i, visited, g)
        ans += 1
print(ans)
