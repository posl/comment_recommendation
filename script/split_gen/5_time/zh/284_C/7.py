def dfs(v):
    seen[v] = True
    for i in range(n):
        if not seen[i] and G[v][i] == 1:
            dfs(i)
n, m = map(int, input().split())
G = [[0] * n for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    G[u-1][v-1] = G[v-1][u-1] = 1
seen = [False] * n
res = 0
for i in range(n):
    if not seen[i]:
        dfs(i)
        res += 1
print(res)
