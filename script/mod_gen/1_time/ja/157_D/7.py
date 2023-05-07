def dfs(start, end, graph, visited):
    visited[start] = True
    if start == end:
        return True
    for node in graph[start]:
        if not visited[node]:
            if dfs(node, end, graph, visited):
                return True
    return False

if __name__ == '__main__':
    dfs()