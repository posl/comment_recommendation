def find_root(tree, x):
    if tree[x] == x:
        return x
    else:
        tree[x] = find_root(tree, tree[x])
        return tree[x]
