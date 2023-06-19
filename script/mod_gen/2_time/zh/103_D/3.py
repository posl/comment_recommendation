def get_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent[x])
        return parent[x]

if __name__ == '__main__':
    get_parent()