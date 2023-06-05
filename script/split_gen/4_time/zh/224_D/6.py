def dfs(v, p, d, G, P):
    P[v] = p
    for i in range(len(G[v])):
        if G[v][i] == p:
            continue
        if P[G[v][i]] == -1:
            dfs(G[v][i], v, d + 1, G, P)
    return
