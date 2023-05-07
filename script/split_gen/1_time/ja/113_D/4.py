def dfs(h,w,k):
    if h == 0:
        if k == w:
            return 1
        else:
            return 0
    elif k == 1:
        return dfs(h-1,w,k+1)
    elif k == w:
        return dfs(h-1,w,k-1)
    else:
        return dfs(h-1,w,k-1) + dfs(h-1,w,k+1)
h,w,k = map(int,input().split())
print(dfs(h,w,k) % 1000000007)
