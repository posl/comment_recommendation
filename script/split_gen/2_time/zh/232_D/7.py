def dfs(graph, start, end):
    visited = []
    stack = [start]
    while stack:
        n = stack.pop()
        if n not in visited:
            if n == end:
                return visited
            visited.append(n)
            stack.extend(graph[n])
    return visited
