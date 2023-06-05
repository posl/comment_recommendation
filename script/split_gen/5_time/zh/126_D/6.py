def dfs(node, color):
    global colors
    colors[node] = color
    for v, w in graph[node]:
        if colors[v] == -1:
            dfs(v, color ^ w % 2)
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))
colors = [-1] * n
dfs(0, 0)
for i in range(n):
    print(colors[i])
