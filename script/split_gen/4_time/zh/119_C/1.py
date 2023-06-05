def dfs(a,b,c,mp):
    global ans
    if a==0 and b==0 and c==0:
        ans=min(ans,mp)
        return
    if a<0 or b<0 or c<0:
        return
    if mp==0:
        for i in range(n):
            dfs(a-l[i],b,c,mp+1)
            dfs(a,b-l[i],c,mp+1)
            dfs(a,b,c-l[i],mp+1)
    else:
        dfs(a-l[i],b,c,mp+1)
        dfs(a,b-l[i],c,mp+1)
        dfs(a,b,c-l[i],mp+1)
        dfs(a-l[i],b-l[i],c,mp+1)
        dfs(a-l[i],b,c-l[i],mp+1)
        dfs(a,b-l[i],c-l[i],mp+1)
        dfs(a-l[i],b-l[i],c-l[i],mp+1)
n,a,b,c=map(int,input().split())
l=[int(input()) for _ in range(n)]
ans=10000
dfs(a,b,c,0)
print(ans)
