def dfs(G, v):
    seen[v] = True
    order.append(v)
    for next_v in G[v]:
        if seen[next_v]: continue
        dfs(G, next_v)
        order.append(v)
N, X, Y = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
seen = [False] * N
order = []
dfs(G, X-1)
print(order)
