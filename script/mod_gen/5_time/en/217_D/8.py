def findParent(parent, i):
    if parent[i] == i:
        return i
    return findParent(parent, parent[i])

if __name__ == '__main__':
    findParent()