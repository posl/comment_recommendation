def dfs(v,p,c):
    color[v] = c
    for i in range(len(G[v])):
        if G[v][i] == p:continue
        if color[G[v][i]] != -1:continue
        dfs(G[v][i],v,c^D[v][i])
N = int(input())
G = [[] for i in range(N)]
D = [[] for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)
    D[u].append(w%2)
    D[v].append(w%2)
color = [-1]*N
dfs(0,-1,0)
for i in range(N):
    print(color[i])
