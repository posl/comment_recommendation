def is_path_graph(n,m,edges):
    if m != n - 1:
        return False
    if max(edges) != n or min(edges) != 1:
        return False
    if len(set(edges)) != n-1:
        return False
    return True
