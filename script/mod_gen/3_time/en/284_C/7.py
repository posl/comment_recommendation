def dfs(G, v, visited):
    visited[v] = True
    for next_v in G[v]:
        if visited[next_v] == False:
            dfs(G, next_v, visited)
