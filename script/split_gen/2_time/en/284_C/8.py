def find_root(x):
    if x == root[x]:
        return x
    else:
        root[x] = find_root(root[x])
        return root[x]
