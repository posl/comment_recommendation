def dfs(v, c):
    global color
    color[v] = c
    for i in range(len(graph[v])):
        if color[graph[v][i]] == c:
            return False
        if color[graph[v][i]] == 0 and not dfs(graph[v][i], -c):
            return False
    return True
