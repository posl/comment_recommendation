def dfs(v, color, c):
    color[v] = c
    for i in range(len(g[v])):
        if color[g[v][i]] == -1:
            dfs(g[v][i], color, c ^ w[v][i])
n = int(input())
g = [[] for i in range(n)]
w = [[] for i in range(n)]
for i in range(n - 1):
    u, v, ww = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    w[u].append(ww % 2)
    w[v].append(ww % 2)
color = [-1] * n
dfs(0, color, 0)
for i in range(n):
    print(color[i])
