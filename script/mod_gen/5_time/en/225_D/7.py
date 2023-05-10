def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

if __name__ == '__main__':
    find_parent()