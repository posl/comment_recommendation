def make_tree(n, a):
    tree = [[] for _ in range(n+1)]
    for i in range(n):
        tree[a[i]].append(i+2)
    return tree

if __name__ == '__main__':
    make_tree()