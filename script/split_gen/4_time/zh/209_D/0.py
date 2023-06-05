def findRoot(x, root):
    if x == root[x]:
        return x
    else:
        root[x] = findRoot(root[x], root)
        return root[x]
