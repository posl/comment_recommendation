def findRoot(root, i):
    if root[i] == i:
        return i
    else:
        root[i] = findRoot(root, root[i])
        return root[i]
