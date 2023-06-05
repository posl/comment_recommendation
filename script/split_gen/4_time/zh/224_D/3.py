def dfs(v, p, d):
    if d == 9:
        return 1
    if d + dist[v][p] > 9:
        return 0
    ret = 0
    for i in range(1, 10):
        if i != p:
            ret += dfs(i, v, d + dist[v][p])
    return ret
