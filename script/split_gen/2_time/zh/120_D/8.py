def findRoot(x):
    global root
    if root[x] == x:
        return x
    else:
        root[x] = findRoot(root[x])
        return root[x]
