def dfs(v, p, d):
    global D
    D[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, d+1)
