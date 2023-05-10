def find_root(node, root):
    if node == root[node]:
        return node
    else:
        root[node] = find_root(root[node], root)
        return root[node]

if __name__ == '__main__':
    find_root()