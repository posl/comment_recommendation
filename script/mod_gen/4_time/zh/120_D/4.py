def findRoot(root, x):
    if root[x] == x:
        return x
    else:
        root[x] = findRoot(root, root[x])
        return root[x]

if __name__ == '__main__':
    findRoot()