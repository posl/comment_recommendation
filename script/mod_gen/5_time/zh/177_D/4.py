def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

if __name__ == '__main__':
    find_set()