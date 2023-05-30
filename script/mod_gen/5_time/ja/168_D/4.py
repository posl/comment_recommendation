def dfs(v, g, seen):
    seen[v] = True
    for next_v in g[v]:
        if seen[next_v]:
            continue
        dfs(next_v, g, seen)
