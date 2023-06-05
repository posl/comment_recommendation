def dfs(v, d):
    global ans
    if d > 8:
        return
    if v == 123456789:
        ans = min(ans, d)
        return
    for i in range(4):
        nv = v + dx[i]
        if nv < 0 or nv >= 9:
            continue
        dfs(nv, d + 1)
M = int(input())
G = [[0 for _ in range(9)] for _ in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u][v] = G[v][u] = 1
P = list(map(int, input().split()))
for i in range(8):
    P[i] -= 1
ans = 9
dx = [1, -1, 3, -3]
for i in range(9):
    for j in range(i + 1, 9):
        if G[i][j] == 0:
            continue
        v = 0
        for k in range(9):
            if k == i:
                v = v * 10 + j
            elif k == j:
                v = v * 10 + i
            else:
                v = v * 10 + k
        dfs(v, 0)
