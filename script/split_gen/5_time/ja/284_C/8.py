def dfs(G, v, seen):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v] == False:
            dfs(G, next_v, seen)
    return seen
