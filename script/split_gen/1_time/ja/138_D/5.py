def dfs(v, p, c):
    ans[v] += c
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v, ans[v])
n, q = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
ans = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    ans[p-1] += x
dfs(0, -1, 0)
print(*ans)
