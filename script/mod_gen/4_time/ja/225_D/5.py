def getRoot(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = getRoot(parent[x])
        return parent[x]

if __name__ == '__main__':
    getRoot()