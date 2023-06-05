def dfs(g, v, u, d, c):
    if d == 0:
        c[v] = 1
        return
    for w in g[v]:
        if w == u:
            continue
        dfs(g, w, v, d - 1, c)
