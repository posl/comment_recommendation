def dfs(v, p, c):
    global color
    color[c] += 1
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v, c)
