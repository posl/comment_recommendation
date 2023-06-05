def dfs(n, x, p, t, c, d):
    for i in t[n]:
        if i != p:
            c[i] += x[n]
            dfs(i, x, n, t, c, d)
    return c
