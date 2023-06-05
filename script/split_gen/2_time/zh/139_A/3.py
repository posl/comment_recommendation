def dfs(u,p):
    global cnt
    cnt[u]+=cnt[p]
    for v in G[u]:
        if v==p:continue
        dfs(v,u)
N,Q = map(int,input().split())
G = [[] for i in range(N)]
cnt = [0]*N
for i in range(N-1):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
for i in range(Q):
    p,x = map(int,input().split())
    p-=1
    cnt[p]+=x
dfs(0,-1)
print(*cnt)
