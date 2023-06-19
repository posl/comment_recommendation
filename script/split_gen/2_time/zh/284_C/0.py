def dfs(v, color, G):
    color[v] = 1
    for i in G[v]:
        if color[i] == 0:
            dfs(i, color, G)
    color[v] = 2
