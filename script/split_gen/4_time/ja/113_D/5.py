def dfs(h,w,k):
    if w == 1:
        return 1
    if k == 1:
        return dfs(h,w-1,k+1)
    elif k == h:
        return dfs(h,w-1,k-1)
    else:
        return dfs(h,w-1,k-1) + dfs(h,w-1,k+1)
h,w,k = map(int,input().split())
print(dfs(h,w,k) % 1000000007)
