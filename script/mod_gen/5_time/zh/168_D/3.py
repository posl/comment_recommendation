def dfs(v):
    global flag
    for i in range(len(g[v])):
        if visited[g[v][i]] == 0:
            visited[g[v][i]] = 1
            if g[v][i] == 1:
                flag = True
                return
            dfs(g[v][i])
            if flag:
                return
        else:
            continue
n,m = map(int,input().split())
g = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
flag = False
visited[1] = 1
dfs(1)
