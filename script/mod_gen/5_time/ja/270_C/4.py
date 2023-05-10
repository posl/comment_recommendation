def dfs(v, p):
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v)
        ans.append(u)
    ans.append(p)
    return
n, x, y = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
ans = []
dfs(x, y)
dfs(y, x)
ans.reverse()
print(*ans)

if __name__ == '__main__':
    dfs()