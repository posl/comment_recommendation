def dfs(v, p=-1):
    global is_tree
    seen[v] = True
    for nv in G[v]:
        if nv == p:
            continue
        if seen[nv]:
            is_tree = False
        else:
            dfs(nv, v)
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
seen = [False] * N
is_tree = True
dfs(0)
for v in range(N):
    if not seen[v]:
        is_tree = False
