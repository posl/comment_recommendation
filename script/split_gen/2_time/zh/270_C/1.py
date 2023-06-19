def dfs(now, prev):
    if now == y:
        print(now, end=" ")
        return True
    for to in edge[now]:
        if to == prev:
            continue
        if dfs(to, now):
            print(now, end=" ")
            return True
    return False
n, x, y = map(int, input().split())
x -= 1
y -= 1
edge = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
dfs(x, -1)
