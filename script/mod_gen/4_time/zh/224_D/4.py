def dfs(now,depth):
    global ans
    if depth>ans:
        return
    if now==0:
        ans=depth
        return
    for i in range(4):
        if 0<=now+di[i]<9 and now+di[i]!=pre:
            pre=now
            dfs(now+di[i],depth+1)
            pre=now
    return
n=int(input())
g=[[] for i in range(9)]
for i in range(n):
    u,v=map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
p=list(map(int,input().split()))
for i in range(8):
    p[i]-=1
ans=100
for i in range(9):
    pre=-1
    dfs(i,0)
