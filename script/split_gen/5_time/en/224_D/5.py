def dfs(v, used, graph):
    used[v] = True
    for i in range(len(graph[v])):
        if used[graph[v][i]] == False:
            dfs(graph[v][i], used, graph)
