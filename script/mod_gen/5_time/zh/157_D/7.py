def dfs(node, visited, graph, result):
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            result[i] = 1
            dfs(i, visited, graph, result)
