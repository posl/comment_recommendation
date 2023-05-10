def find_set(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_set(parent[x])
        return parent[x]
