def dfs(g, s, visited):
    visited[s] = True
    for t in g[s]:
        if visited[t] == False:
            dfs(g, t, visited)

if __name__ == '__main__':
    dfs()