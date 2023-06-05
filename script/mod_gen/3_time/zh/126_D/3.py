def dfs(s, v, c):
    color[v] = c
    for i in range(len(graph[v])):
        if color[graph[v][i]] == -1:
            if not dfs(s, graph[v][i], c ^ 1):
                return False
        elif color[graph[v][i]] == c:
            return False
    return True

if __name__ == '__main__':
    dfs()