def dfs(v, p, x):
    global ans
    ans[v] += x
    for i in G[v]:
        if i != p:
            dfs(i, v, x)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
ans = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    dfs(p-1, -1, x)
print(*ans)
