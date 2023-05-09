def find_root(x):
    if x == root[x]:
        return x
    else:
        root[x] = find_root(root[x])
        return root[x]

if __name__ == '__main__':
    find_root()