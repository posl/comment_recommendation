def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        if root_x > root_y:
            parent[root_x] += parent[root_y]
            parent[root_y] = root_x
        else:
            parent[root_y] += parent[root_x]
            parent[root_x] = root_y

if __name__ == '__main__':
    union()