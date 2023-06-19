def dfs(graph, v, seen):
    seen[v] = True
    for next_v in graph[v]:
        if seen[next_v]:
            continue
        dfs(graph, next_v, seen)
