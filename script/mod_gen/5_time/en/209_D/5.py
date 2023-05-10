def find_root(x, parent):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_root(parent[x], parent)
        return parent[x]

if __name__ == '__main__':
    find_root()