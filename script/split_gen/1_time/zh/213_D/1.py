def dfs(v, p):
    global ans
    ans.append(v)
    for i in g[v]:
        if i != p:
            dfs(i, v)
            ans.append(v)
N = int(input())
g = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
for i in range(N):
    g[i].sort()
ans = []
dfs(0, -1)
print(*[i + 1 for i in ans])
