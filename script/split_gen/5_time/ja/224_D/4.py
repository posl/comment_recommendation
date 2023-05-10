def dfs(v, g, visited):
    visited[v] = True
    for next_v in g[v]:
        if visited[next_v]:
            continue
        dfs(next_v, g, visited)
    return visited
