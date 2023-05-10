def get_parent(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent, parent[x])
        return parent[x]
