def dfs(h,w,k):
    if w==1:
        if k==1:
            return 1
        else:
            return 0
    elif k==1:
        return dfs(h-1,w-1,1)
    elif k==w:
        return dfs(h-1,w-1,w-1)
    else:
        return dfs(h-1,w-1,k-1)+dfs(h-1,w-1,k)*(w-k)

if __name__ == '__main__':
    dfs()