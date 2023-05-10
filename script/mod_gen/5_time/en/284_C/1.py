def find_parent(parent, i):
    if parent[i] == -1:
        return i
    if parent[i] != -1:
        return find_parent(parent, parent[i])

if __name__ == '__main__':
    find_parent()