def find_path(u,v):
    path = []
    while u != v:
        path.append(u)
        u = parent[u]
    path.append(v)
    return path
