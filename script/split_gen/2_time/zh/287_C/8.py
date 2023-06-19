def isPathGraph(n, m, edges):
    if m != n-1:
        return False
    edges = sorted(edges, key=lambda x: x[0])
    for i in range(0, n-1):
        if edges[i][0] != i+1 or edges[i][1] != i+2:
            return False
    return True
