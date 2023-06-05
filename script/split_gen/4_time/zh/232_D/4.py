def dfs(i,j):
    if i==h-1 and j==w-1:
        return 1
    if i==h-1:
        if a[i][j+1]=='#':
            return 1
        else:
            return dfs(i,j+1)
    if j==w-1:
        if a[i+1][j]=='#':
            return 1
        else:
            return dfs(i+1,j)
    if a[i+1][j]=='#' and a[i][j+1]=='#':
        return 1
    elif a[i+1][j]=='#':
        return dfs(i,j+1)
    elif a[i][j+1]=='#':
        return dfs(i+1,j)
    else:
        return dfs(i,j+1)+dfs(i+1,j)
h,w=map(int,input().split())
a=[list(input()) for _ in range(h)]
print(dfs(0,0))
