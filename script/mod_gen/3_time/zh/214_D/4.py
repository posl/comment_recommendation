def find_root(u):
    if u == root[u]:
        return u
    else:
        root[u] = find_root(root[u])
        return root[u]

if __name__ == '__main__':
    find_root()