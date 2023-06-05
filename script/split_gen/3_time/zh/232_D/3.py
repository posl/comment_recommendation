def dfs(i,j):
    if i==H-1 and j==W-1:
        return 1
    if i==H-1:
        if grid[i][j+1]=='#':
            return 1
        else:
            return dfs(i,j+1)+1
    if j==W-1:
        if grid[i+1][j]=='#':
            return 1
        else:
            return dfs(i+1,j)+1
    if grid[i+1][j]=='#':
        return dfs(i,j+1)+1
    if grid[i][j+1]=='#':
        return dfs(i+1,j)+1
    return max(dfs(i+1,j),dfs(i,j+1))+1
H,W=map(int,input().split())
grid=[]
for i in range(H):
    grid.append(list(input()))
print(dfs(0,0))
