def dfs(v, p):
    ans.append(v)
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v)
        ans.append(v)
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
for i in range(n):
    g[i].sort()
ans = []
dfs(0, -1)
print(*[x+1 for x in ans])
