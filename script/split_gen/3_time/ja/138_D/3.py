def dfs(v, p=-1):
    for nv in G[v]:
        if nv == p:
            continue
        ans[nv] += ans[v]
        dfs(nv, v)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
ans = [0] * N
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
for _ in range(Q):
    p, x = map(int, input().split())
    ans[p-1] += x
dfs(0)
print(*ans)
