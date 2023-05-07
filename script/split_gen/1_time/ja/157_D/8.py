def dfs(u, color):
    color[u] = 1
    for v in edge[u]:
        if color[v] == 0:
            dfs(v, color)
