def dfs(v, p, d):
    if d == 8: return 0
    res = 100
    for i in range(1, 10):
        if i == p: continue
        res = min(res, dfs(i, v, d + 1) + 1)
    return res
M = int(input())
G = [[] for i in range(9)]
for i in range(M):
    u, v = map(int, input().split())
    G[u - 1].append(v - 1)
    G[v - 1].append(u - 1)
P = list(map(int, input().split()))
res = 100
for i in range(1, 10):
    res = min(res, dfs(i, -1, 0))
print(res if res < 100 else -1)
