def dfs(v,p,c):
    color[v] = c
    for e in G[v]:
        if e[0] == p:
            continue
        if e[1] % 2 == 0:
            dfs(e[0],v,c)
        else:
            dfs(e[0],v,1-c)
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    G[u].append((v,w))
    G[v].append((u,w))
color = [0]*N
dfs(0,-1,0)
print("\n".join(map(str,color)))
