def dfs(v, p, d):
    depth[v] = d
    for u in graph[v]:
        if u == p:
            continue
        dfs(u, v, d + 1)
