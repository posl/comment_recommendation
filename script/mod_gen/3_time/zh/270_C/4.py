def find_path(u,v):
    path = []
    while u != v:
        path.append(u)
        u = parent[u]
    path.append(v)
    return path

if __name__ == '__main__':
    find_path()