def dfs(v,p):
    for u in edge[v]:
        if u==p:
            continue
        cnt[u]+=cnt[v]
        dfs(u,v)
n,q=map(int,input().split())
edge=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
cnt=[0]*n
for _ in range(q):
    p,x=map(int,input().split())
    cnt[p-1]+=x
dfs(0,-1)
print(*cnt)
