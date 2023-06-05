def dfs(u, p):
    global ans
    for v in g[u]:
        if v == p:
            continue
        if v in s:
            ans[v] -= 1
        else:
            ans[v] += 1
        dfs(v, u)
n, m, k = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
s = set()
for _ in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if c > d:
        c, d = d, c
    if c == 0 and d == n - 1:
        s.add(d)
    else:
        g[c].append(d)
        g[d].append(c)
ans = [0] * n
dfs(0, -1)
print(*ans)

if __name__ == '__main__':
    dfs()