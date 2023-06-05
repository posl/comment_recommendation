def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
