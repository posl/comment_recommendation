def find_set(a):
    if a != parent[a]:
        parent[a] = find_set(parent[a])
    return parent[a]

if __name__ == '__main__':
    find_set()