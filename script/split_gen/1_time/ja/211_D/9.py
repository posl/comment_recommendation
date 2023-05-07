def dfs(G, s):
    # s: start node
    # G: adjacency list
    # R: return value
    # V: visited
    # P: previous
    # D: distance
    # L: layer
    R = {}
    V = [False] * len(G)
    P = [-1] * len(G)
    D = [0] * len(G)
    L = [0] * len(G)
    def dfs_visit(G, u):
        V[u] = True
        for v in G[u]:
            if not V[v]:
                P[v] = u
                D[v] = D[u] + 1
                L[v] = L[u] + 1
                dfs_visit(G, v)
    dfs_visit(G, s)
    R['V'] = V
    R['P'] = P
    R['D'] = D
    R['L'] = L
    return R
