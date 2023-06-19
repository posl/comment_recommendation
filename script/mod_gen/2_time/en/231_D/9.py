def dfs(g, s, visited):
    visited[s] = True
    for t in g[s]:
        if visited[t] == False:
            dfs(g, t, visited)
