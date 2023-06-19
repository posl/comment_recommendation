def dfs(h,w):
    if h==H:
        return w==K
    elif w==1:
        return dfs(h+1,w+1)
    elif w==W:
        return dfs(h+1,w-1)
    else:
        return dfs(h+1,w+1)+dfs(h+1,w-1)
H,W,K=map(int,input().split())
print(dfs(0,1)%1000000007)
