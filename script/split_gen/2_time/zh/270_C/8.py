def dfs(v,p):
    global ans
    ans.append(v)
    for u in G[v]:
        if u != p:
            dfs(u,v)
            ans.append(v)
    return
N,X,Y = map(int,input().split())
U = [0]*(N-1)
V = [0]*(N-1)
for i in range(N-1):
    U[i],V[i] = map(int,input().split())
G = [[] for _ in range(N+1)]
for i in range(N-1):
    G[U[i]].append(V[i])
    G[V[i]].append(U[i])
ans = []
dfs(X,-1)
ans.append(X)
ans.reverse()
ans.append(Y)
print(*ans)
