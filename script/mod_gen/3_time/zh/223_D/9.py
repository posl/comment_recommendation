def dfs(v):
    global g, used, vs, vs2, N
    used[v] = True
    for i in range(N):
        if g[v][i] == 1 and used[i] == False:
            dfs(i)
    vs.append(v)
    vs2.append(v)

if __name__ == '__main__':
    dfs()