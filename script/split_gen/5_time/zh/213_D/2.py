def dfs(v, p):
    order.append(v)
    for nv in G[v]:
        if nv == p: continue
        dfs(nv, v)
        order.append(v)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
order = []
dfs(0, -1)
print(' '.join(map(lambda x: str(x+1), order)))
