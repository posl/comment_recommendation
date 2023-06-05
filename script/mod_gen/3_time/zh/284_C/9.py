def dfs(v):
    global seen,graph
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(next_v)
