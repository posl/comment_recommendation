def get_subtree_size(g, i):
    def _get_subtree_size(g, i, visited):
        visited.add(i)
        size = 1
        for j in g[i]:
            if j not in visited:
                size += _get_subtree_size(g, j, visited)
        return size
    return _get_subtree_size(g, i, set())
