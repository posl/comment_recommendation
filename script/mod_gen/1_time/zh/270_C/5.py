def dfs(v):
    global path
    global visited
    global G
    global N
    global X
    global Y
    global flag
    if flag == 1:
        return
    path.append(v)
    visited[v] = True
    if v == Y:
        flag = 1
        for i in path:
            print(i,end=' ')
        return
    for next_v in G[v]:
        if visited[next_v] == False:
            dfs(next_v)
            path.pop()
N,X,Y = map(int,input().split())
X -= 1
Y -= 1
G = [[] for i in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
visited = [False]*N
path = []
flag = 0
dfs(X)
