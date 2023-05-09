def make_tree(n, a):
    tree = [[] for _ in range(n+1)]
    for i in range(n):
        tree[a[i]].append(i+2)
    return tree
