def find_root(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_root(parent[x])
        return parent[x]

if __name__ == '__main__':
    find_root()