def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

if __name__ == '__main__':
    find()