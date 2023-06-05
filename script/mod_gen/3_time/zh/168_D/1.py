def dfs(x):
    global flag
    if flag:
        return
    if visited[x]:
        return
    visited[x] = True
    for i in range(len(g[x])):
        if g[x][i] == 1:
            dfs(i)
            if flag:
                path[x] = i
                return
    visited[x] = False

if __name__ == '__main__':
    dfs()