def dfs(v,p,c):
    color[v]=c
    for i in g[v]:
        if i==p:continue
        if color[i]==c:return 1
        if color[i]==0 and dfs(i,v,-c):return 1
    return 0
n,q=map(int,input().split())
g=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
color=[0]*n
dfs(0,-1,1)
for _ in range(q):
    c,d=map(int,input().split())
    if color[c-1]==color[d-1]:print("Town")
    else:print("Road")
