def find_parent(parent, node):
    if parent[node] == None:
        return 1
    else:
        return 1 + find_parent(parent, parent[node])

if __name__ == '__main__':
    find_parent()