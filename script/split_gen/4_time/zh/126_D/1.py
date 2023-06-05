def dfs(u, color):
    visited[u] = True
    colors[u] = color
    for v, w in G[u]:
        if not visited[v]:
            dfs(v, color ^ (w & 1))
N = int(input())
G = [[] for i in range(N)]
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))
visited = [False] * N
colors = [0] * N
dfs(0, 0)
print("\n".join(map(str, colors)))
