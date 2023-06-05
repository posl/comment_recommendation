def dfs(u, color):
    color[u] = 1
    for v, w in edges[u]:
        if color[v] == -1:
            color[v] = color[u] ^ w
            dfs(v, color)
n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, w % 2))
    edges[v].append((u, w % 2))
color = [-1] * n
dfs(0, color)
print(*color, sep='\n')
