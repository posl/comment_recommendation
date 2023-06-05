def dfs(u, color, G):
    color[u] = 1
    for v in G[u]:
        if color[v] == 0:
            dfs(v, color, G)
    color[u] = 2
