def dfs(v, p):
    for u in graph[v]:
        if u == p: continue
        dist[u] = dist[v] + 1
        dfs(u, v)
n, x, y = map(int, input().split())
x -= 1
y -= 1
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
dist = [0] * n
dfs(x, -1)
print(*dist)

if __name__ == '__main__':
    dfs()