def dfs(u, c, color):
    color[u] = c
    for v, w in edge[u]:
        if color[v] == -1:
            dfs(v, c ^ w % 2, color)
n = int(input())
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    edge[u - 1].append((v - 1, w))
    edge[v - 1].append((u - 1, w))
color = [-1] * n
dfs(0, 0, color)
for c in color:
    print(c)
