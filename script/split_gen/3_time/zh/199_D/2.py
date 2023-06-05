def dfs(v, c):
    color[v] = c
    for i in range(n):
        if G[v][i] == 0:
            continue
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
n, m = map(int, input().split())
G = [[0 for _ in range(n)] for _ in range(n)]
color = [0 for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1
