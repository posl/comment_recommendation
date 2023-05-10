def dfs(u, par):
    global ans
    ans.append(u)
    for v in edge[u]:
        if v != par:
            dfs(v, u)
            ans.append(u)
    return
n, x, y = map(int, input().split())
edge = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)
ans = []
dfs(x, -1)
print(*ans)
