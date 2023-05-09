def dfs(v, p):
    for u in g[v]:
        if u == p:
            continue
        d[u] = v
        dfs(u, v)
n, x, y = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
d = [0] * (n + 1)
dfs(x, -1)
ans = [y]
while y != x:
    y = d[y]
    ans.append(y)
print(*ans[::-1])

if __name__ == '__main__':
    dfs()