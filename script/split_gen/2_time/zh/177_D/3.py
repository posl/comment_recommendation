def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]
