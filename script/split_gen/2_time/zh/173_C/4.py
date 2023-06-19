def dfs(h, w, k, c):
    if h == 0 and w == 0:
        if k == 0:
            return 1
        else:
            return 0
    elif h == 0:
        return dfs(h, w-1, k, c)
    elif w == 0:
        return dfs(h-1, w, k, c)
    elif c[h-1][w-1] == "#":
        return dfs(h-1, w, k, c) + dfs(h, w-1, k, c)
    else:
        return dfs(h-1, w, k, c) + dfs(h, w-1, k, c) + dfs(h-1, w-1, k-1, c)
