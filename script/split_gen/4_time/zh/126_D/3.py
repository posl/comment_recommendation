def dfs(u, color):
    color[u] = 1
    for i in range(len(graph[u])):
        v = graph[u][i][0]
        w = graph[u][i][1]
        if color[v] == -1:
            if w % 2 == 0:
                color[v] = color[u]
            else:
                color[v] = 1 - color[u]
            dfs(v, color)
n = int(input())
graph = [[] for i in range(n)]
color = [-1 for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append([v, w])
    graph[v].append([u, w])
dfs(0, color)
for i in range(n):
    print(color[i])
