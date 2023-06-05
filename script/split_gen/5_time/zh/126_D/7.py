def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        if color[G[v][i]] == -1:
            dfs(G[v][i], 1 - c)
N = int(input())
G = [[] for _ in range(N)]
color = [-1] * N
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w % 2 == 0:
        G[u].append(v)
        G[v].append(u)
dfs(0, 0)
for i in range(N):
    print(color[i])
