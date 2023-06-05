def dfs(n, m, path, result):
    if len(path) == n:
        result.append(path)
        return
    for i in range(1, m+1):
        if len(path) == 0 or i > path[-1]:
            dfs(n, m, path+[i], result)
