def dfs(u, p):
    for v in edge[u]:
        if v == p:
            continue
        path.append(v)
        dfs(v, u)
        path.append(u)
n, x, y = map(int, input().split())
edge = [[] for i in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    edge[u].append(v)
    edge[v].append(u)
path = [x]
dfs(x, 0)
path.append(x)
path = path[path.index(y):]
print(*path)
