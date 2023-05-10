def findParent(parent, i):
    if parent[i] == i:
        return i
    return findParent(parent, parent[i])
