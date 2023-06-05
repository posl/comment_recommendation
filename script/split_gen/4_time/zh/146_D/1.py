def dfs(v,p=-1):
    global k
    c = 1
    for u in g[v]:
        if u==p:continue
        if c==c1 or c==p1:c+=1
        ans[u] = c
        c1,p1 = c,p
        c+=1
        k = max(k,c)
        dfs(u,v)
n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
ans = [0]*(n+1)
k = 0
dfs(1)
print(k)
for i in range(1,n):
    print(ans[i])
