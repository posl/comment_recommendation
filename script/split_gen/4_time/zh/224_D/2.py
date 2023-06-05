def dfs(v, d, p):
    global ans
    if d > 16:
        return
    if v == 9:
        ans = min(ans, d)
        return
    for i in range(8):
        if p[i] == v:
            p[i] = 0
            dfs(i + 1, d + 1, p)
            p[i] = v
