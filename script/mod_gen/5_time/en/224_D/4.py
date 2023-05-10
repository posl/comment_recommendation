def dfs(graph, v, visited):
    visited[v] = True
    for i in range(1, 10):
        if graph[v][i] and not visited[i]:
            dfs(graph, i, visited)

if __name__ == '__main__':
    dfs()