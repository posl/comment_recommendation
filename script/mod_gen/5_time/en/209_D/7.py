def find_root(x):
    global root
    if root[x] == x:
        return x
    else:
        root[x] = find_root(root[x])
        return root[x]

if __name__ == '__main__':
    find_root()