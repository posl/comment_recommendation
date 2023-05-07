def dfs(v, c):
    global ans
    if v == n:
        ans += 1
        return
    for i in range(3):
        if c[v][i] == 0:
            for j in g[v]:
                c[j][i] += 1
            dfs(v + 1, c)
            for j in g[v]:
                c[j][i] -= 1
n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
ans = 0
c = [[0] * 3 for i in range(n)]
dfs(0, c)
print(ans)
