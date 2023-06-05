def dfs(v):
    seen[v] = True
    for nv in g[v]:
        if seen[nv]:
            continue
        dfs(nv)
