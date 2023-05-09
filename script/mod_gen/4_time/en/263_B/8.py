def get_parent_count(parents, child):
    parent = parents[child]
    if parent == 1:
        return 1
    return 1 + get_parent_count(parents, parent)

if __name__ == '__main__':
    get_parent_count()