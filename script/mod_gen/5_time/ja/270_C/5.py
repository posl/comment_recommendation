def dfs(v, p):
    global ans
    ans.append(v)
    for i in g[v]:
        if i == p:
            continue
        dfs(i, v)
        ans.append(v)
    return
n, x, y = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
ans = []
dfs(x, -1)
ans.append(x)
dfs(y, -1)
ans.append(y)
print(*ans)

if __name__ == '__main__':
    dfs()