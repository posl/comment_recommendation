def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]
