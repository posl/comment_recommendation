def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == -1:
            dfs(G[v][i], c ^ 1)
N = int(input())
G = [[] for i in range(N)]
color = [-1] * N
for i in range(N - 1):
    u, v, w = [int(x) for x in input().split()]
    u -= 1
    v -= 1
    if w % 2 == 0:
        G[u].append(v)
        G[v].append(u)
dfs(0, 0)
for i in range(N):
    print(color[i])
