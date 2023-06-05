def findRoot(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = findRoot(parent, parent[x])
        return parent[x]

if __name__ == '__main__':
    findRoot()