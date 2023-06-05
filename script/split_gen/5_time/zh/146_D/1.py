def dfs1(G, v, p, d, c):
    c[v] = d
    for u in G[v]:
        if u == p:
            continue
        dfs1(G, u, v, d + 1, c)
