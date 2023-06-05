def find_root(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_root(parent[x])
        return parent[x]
