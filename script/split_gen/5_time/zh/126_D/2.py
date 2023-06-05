def dfs(u, c):
    color[u] = c
    for i in range(len(G[u])):
        v = G[u][i][0]
        if color[v] == -1:
            if G[u][i][1] % 2 == 0:
                dfs(v, c)
            else:
                dfs(v, 1 - c)
N = int(input())
G = [[] for i in range(N)]
color = [-1 for i in range(N)]
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))
dfs(0, 0)
for i in range(N):
    print(color[i])
