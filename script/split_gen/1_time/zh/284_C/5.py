def dfs(v):
    seen[v] = True
    for i in range(n):
        if not seen[i] and G[v][i] == 1:
            dfs(i)
n, m = map(int, input().split())
G = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a-1][b-1] = G[b-1][a-1] = 1
seen = [False for _ in range(n)]
res = 0
for i in range(n):
    if not seen[i]:
        dfs(i)
        res += 1
print(res)
