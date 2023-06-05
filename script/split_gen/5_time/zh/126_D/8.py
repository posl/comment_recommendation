def dfs(s, c):
    color[s] = c
    for i in range(len(g[s])):
        if color[g[s][i]] == -1:
            dfs(g[s][i], c ^ d[s][i])
n = int(input())
g = [[] for _ in range(n)]
d = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)
    d[u - 1].append(w % 2)
    d[v - 1].append(w % 2)
color = [-1] * n
dfs(0, 0)
for i in range(n):
    print(color[i])
