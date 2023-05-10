def dfs(v, c):
    color[v] = c
    for i in range(len(edge[v])):
        if color[edge[v][i]] == -1:
            dfs(edge[v][i], c ^ 1)
n = int(input())
edge = [[] for i in range(n)]
color = [-1 for i in range(n)]
for i in range(n - 1):
    a, b, w = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
dfs(0, 0)
for i in range(n):
    print(color[i])
