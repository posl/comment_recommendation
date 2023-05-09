def dfs(v,p):
    for u in g[v]:
        if u==p:
            continue
        cnt[u]+=cnt[v]
        dfs(u,v)
n,q=map(int,input().split())
g=[[] for _ in range(n)]
cnt=[0]*n
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
for _ in range(q):
    p,x=map(int,input().split())
    cnt[p-1]+=x
dfs(0,-1)
print(*cnt)

if __name__ == '__main__':
    dfs()