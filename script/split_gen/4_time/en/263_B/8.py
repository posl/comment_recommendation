def get_parent_count(parents, child):
    parent = parents[child]
    if parent == 1:
        return 1
    return 1 + get_parent_count(parents, parent)
