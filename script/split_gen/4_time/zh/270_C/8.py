def get_tree_paths(tree, start, end):
    paths = []
    for i in range(len(tree)):
        if tree[i][0] == start:
            if tree[i][1] == end:
                paths.append([start, end])
            else:
                sub_paths = get_tree_paths(tree, tree[i][1], end)
                for sub_path in sub_paths:
                    paths.append([start] + sub_path)
        elif tree[i][1] == start:
            if tree[i][0] == end:
                paths.append([start, end])
            else:
                sub_paths = get_tree_paths(tree, tree[i][0], end)
                for sub_path in sub_paths:
                    paths.append([start] + sub_path)
    return paths
