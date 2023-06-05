def build_tree(edges):
    tree = {}
    for edge in edges:
        if edge[0] not in tree.keys():
            tree[edge[0]] = []
        if edge[1] not in tree.keys():
            tree[edge[1]] = []
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    return tree
