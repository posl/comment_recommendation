def dfs(a,b,c,mp):
    global ans
    if a==0 and b==0 and c==0:
        ans=min(ans,mp)
        return
    if mp>ans:
        return
    if a>0:
        dfs(a-1,b,c,mp+10)
    if b>0:
        dfs(a,b-1,c,mp+10)
    if c>0:
        dfs(a,b,c-1,mp+10)
    if a>0 and b>0:
        dfs(a-1,b-1,c,mp+10)
    if b>0 and c>0:
        dfs(a,b-1,c-1,mp+10)
    if c>0 and a>0:
        dfs(a-1,b,c-1,mp+10)
    if a>0 and b>0 and c>0:
        dfs(a-1,b-1,c-1,mp+10)
    if a>0:
        dfs(a-1,b,c,mp+1)
    if b>0:
        dfs(a,b-1,c,mp+1)
    if c>0:
        dfs(a,b,c-1,mp+1)
    if a>1:
        dfs(a-2,b,c,mp+1)
    if b>1:
        dfs(a,b-2,c,mp+1)
    if c>1:
        dfs(a,b,c-2,mp+1)
    if a>0 and b>0:
        dfs(a-1,b-1,c,mp+1)
    if b>0 and c>0:
        dfs(a,b-1,c-1,mp+1)
    if c>0 and a>0:
        dfs(a-1,b,c-1,mp+1)
    if a>0 and b>1:
        dfs(a-1,b-2,c,mp+1)
    if b>0 and c>1:
        dfs(a,b-1,c-2,mp+1)
    if c>0 and a>1:
        dfs(a-2,b,c-1,mp+1)
    if a>1 and b>0:
        dfs(a-2,b-1,c,mp+1)
    if b>1 and c>0:
        dfs(a,b-2,c-1,mp+1)
