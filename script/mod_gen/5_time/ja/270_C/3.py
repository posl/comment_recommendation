def dfs(v,parent):
    for u in g[v]:
        if u==parent:
            continue
        else:
            depth[u]=depth[v]+1
            dfs(u,v)
n,x,y=map(int,input().split())
x-=1
y-=1
g=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1
    g[a].append(b)
    g[b].append(a)
depth=[0]*n
dfs(x,-1)
ans=[0]*n
for i in range(n):
    ans[depth[i]]+=1
print(ans[depth[y]]-1)

if __name__ == '__main__':
    dfs()