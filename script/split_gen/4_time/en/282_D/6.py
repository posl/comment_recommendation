def dfs(graph, v, color):
    color[v] = 1
    for i in graph[v]:
        if color[i] == 0:
            dfs(graph, i, color)
        elif color[i] == 1:
            return False
    color[v] = 2
    return True
n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
color = [0 for i in range(n)]
ans = 0
for i in range(n):
    if color[i] == 0:
        if dfs(graph, i, color):
            ans += 1
print(ans)
