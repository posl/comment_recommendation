def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])
