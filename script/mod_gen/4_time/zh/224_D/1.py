def dfs(v, visited, G, P):
    visited[v] = True
    for i in range(len(G[v])):
        if visited[G[v][i]] == False:
            dfs(G[v][i], visited, G, P)
    return visited

if __name__ == '__main__':
    dfs()