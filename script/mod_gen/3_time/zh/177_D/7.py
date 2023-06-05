def union(x, y):
    x = find(x)
    y = find(y)
    if (x == y):
        return
    if (rank[x] < rank[y]):
        parent[x] = y
    else:
        parent[y] = x
        if (rank[x] == rank[y]):
            rank[x] += 1

if __name__ == '__main__':
    union()