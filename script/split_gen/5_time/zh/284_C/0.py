def dfs(i, used, graph):
    used[i] = True
    for j in graph[i]:
        if not used[j]:
            dfs(j, used, graph)
