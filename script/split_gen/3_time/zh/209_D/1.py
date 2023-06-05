def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])
