def isPathGraph(n, m, u, v):
    if m != n-1:
        return False
    for i in range(m):
        if abs(u[i]-v[i]) != 1:
            return False
    return True
