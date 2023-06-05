def dfs(u,p):
    for v in g[u]:
        if v==p:continue
        cnt[v]+=cnt[u]
        dfs(v,u)
n,q=map(int,input().split())
g=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a].append(b)
    g[b].append(a)
cnt=[0]*(n+1)
for _ in range(q):
    p,x=map(int,input().split())
    cnt[p]+=x
dfs(1,-1)
print(*cnt[1:])
