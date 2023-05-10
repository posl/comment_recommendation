def add_to_tree(tree, parent, child, value):
    if parent in tree:
        tree[parent].append((child, value))
    else:
        tree[parent] = [(child, value)]

if __name__ == '__main__':
    add_to_tree()