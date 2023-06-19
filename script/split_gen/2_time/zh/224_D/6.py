def dfs(v, p, d):
    if d == 9:
        return 1
    if v == p[d]:
        return dfs(v, p, d+1)
    return dfs(p[d], p, d+1) + 1
