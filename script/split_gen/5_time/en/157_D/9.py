def dfs(G, s, a, b):
    if s == b:
        return True
    for t in G[s]:
        if t == a or t == b:
            continue
        if dfs(G, t, a, b):
            return True
    return False
