def dfs(u):
    seen[u] = True
    res[u] += add[u]
    for v in adj[u]:
        if not seen[v]:
            add[v] += add[u]
            dfs(v)
n, q = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
res = [0] * (n+1)
add = [0] * (n+1)
seen = [False] * (n+1)
for _ in range(q):
    p, x = map(int, input().split())
    add[p] += x
dfs(1)
print(*res[1:])
