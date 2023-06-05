def dfs(i,j):
    if i==h-1 and j==w-1:
        return 1
    if i>h-1 or j>w-1:
        return 0
    if grid[i][j]==1:
        return 0
    grid[i][j]=1
    return dfs(i+1,j)+dfs(i,j+1)
h,w=map(int,input().split())
grid=[[0]*w for _ in range(h)]
for i in range(h):
    s=input()
    for j in range(w):
        if s[j]=='#':
            grid[i][j]=1
print(dfs(0,0))
