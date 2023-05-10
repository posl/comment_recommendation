def paint_tree(tree, color, node, parent, dist):
    color[node] = (color[parent] + dist) % 2
    for child, dist in tree[node]:
        if child == parent:
            continue
        paint_tree(tree, color, child, node, dist)

if __name__ == '__main__':
    paint_tree()