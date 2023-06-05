def dfs(i, v, g, visited):
    visited[i] = v
    for j in g[i]:
        if visited[j] == -1:
            dfs(j, v, g, visited)
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
visited1 = [-1] * n
visited2 = [-1] * n
dfs(0, 0, g, visited1)
dfs(0, 1, g, visited2)
print("Yes" if visited1 == visited2 else "No")
