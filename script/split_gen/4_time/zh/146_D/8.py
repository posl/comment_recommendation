def dfs(v, p, c):
    color = 1
    for u in g[v]:
        if u == p:
            continue
        if color == c:
            color += 1
        ans[(v, u)] = ans[(u, v)] = color
        dfs(u, v, color)
        color += 1
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
ans = {}
dfs(0, -1, -1)
print(max(ans.values()))
for i in range(n - 1):
    print(ans[(i, i + 1)])
