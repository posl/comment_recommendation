def dfs(x, c):
    color[x] = c
    for y, w in edges[x]:
        if color[y] == -1:
            dfs(y, c ^ w)
n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    edges[u - 1].append((v - 1, w % 2))
    edges[v - 1].append((u - 1, w % 2))
color = [-1] * n
dfs(0, 0)
for i in range(n):
    print(color[i])
