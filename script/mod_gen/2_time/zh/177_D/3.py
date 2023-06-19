def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

if __name__ == '__main__':
    find()