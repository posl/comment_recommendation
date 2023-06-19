def dfs(v,p,c):
    color[c] = True
    for i in g[v]:
        if i == p:
            continue
        for j in range(1,k+1):
            if not color[j]:
                ans[i] = j
                dfs(i,v,j)
                break
n = int(input())
g = [[] for _ in range(n+1)]
ans = [0] * (n+1)
color = [False] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
k = 0
for i in range(1,n+1):
    k = max(k,len(g[i]))
print(k)
ans[1] = 1
dfs(1,-1,1)
for i in range(1,n+1):
    print(ans[i])
