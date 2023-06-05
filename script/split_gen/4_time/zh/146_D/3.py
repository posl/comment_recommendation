def dfs(v,p):
    c = 1
    for i in g[v]:
        if i == p:
            continue
        if c == color[p]:
            c += 1
        color[i] = c
        dfs(i,v)
        c += 1
n = int(input())
g = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)
color = [0] * (n+1)
dfs(1,0)
print(max(color))
for i in range(1,n):
    print(color[i])
