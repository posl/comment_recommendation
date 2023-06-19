def dfs(p,q):
    if len(p) == 0:
        return 0
    else:
        return dfs(p[1:],q[1:]) + (p[0] - q[0])**2
