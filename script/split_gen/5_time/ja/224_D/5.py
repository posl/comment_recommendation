def dfs(v, p, g):
    if v == 0:
        return 0
    if v == 1:
        return 1
    ret = 0
    for e in g[v]:
        if e != p:
            ret = max(ret, dfs(e, v, g))
    return ret + 1
