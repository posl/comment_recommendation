def dfs(v, p, c):
    color[v] = c
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        if L[i] % 2 == 0:
            dfs(G[v][i], v, c)
        else:
            dfs(G[v][i], v, 1 - c)
n = int(input())
G = [[] for _ in range(n)]
L = [0] * (n - 1)
color = [0] * n
for i in range(n - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    L[i] = w
dfs(0, -1, 0)
for i in range(n):
    print(color[i])
