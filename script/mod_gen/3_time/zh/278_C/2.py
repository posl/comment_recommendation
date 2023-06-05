def find(a):
    if a == root[a]:
        return a
    else:
        root[a] = find(root[a])
        return root[a]

if __name__ == '__main__':
    find()