def dfs(h,w):
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                dfs(i,j)
