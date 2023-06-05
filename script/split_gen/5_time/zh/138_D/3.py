def dfs(v, p, d):
    global c
    global ans
    c[v] += d
    ans[v-1] += c[v]
    for i in range(len(g[v])):
        if g[v][i] != p:
            dfs(g[v][i], v, d)
n, q = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
c = [0] * (n+1)
ans = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    dfs(p, -1, x)
print(*ans)
