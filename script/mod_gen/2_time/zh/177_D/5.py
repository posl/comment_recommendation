def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

if __name__ == '__main__':
    find()