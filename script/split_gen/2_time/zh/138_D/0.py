def tree_add(tree, v, x):
    tree[v] += x
    for i in range(1, len(tree)):
        if tree[i] == v:
            tree_add(tree, i, x)
    return tree
