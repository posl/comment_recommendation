def find_root(x):
    if root[x] == x:
        return x
    else:
        root[x] = find_root(root[x])
        return root[x]
