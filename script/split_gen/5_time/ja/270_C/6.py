def dfs(v, p, g, d, ans):
    ans.append(v)
    for u in g[v]:
        if u == p:
            continue
        if d[u] == -1:
            d[u] = d[v] + 1
            dfs(u, v, g, d, ans)
            ans.append(v)
            d[v] = d[u] + 1
            return
    ans.pop()
n, x, y = map(int, input().split())
x -= 1
y -= 1
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
d = [-1] * n
d[x] = 0
ans = []
dfs(y, -1, g, d, ans)
print(*[v + 1 for v in ans])
