def main():
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        a, b = map(int, input().split())
        bridges.append((min(a, b), max(a, b)))
    bridges = bridges[::-1]
    # disjoint set
    parent = [i for i in range(N + 1)]
    size = [1 for _ in range(N + 1)]
    def find(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = find(parent[x])
            return parent[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]
        return
    # count
    count = 0
    for i in range(1, N + 1):
        count += size[find(i)] - 1
    for i in range(M):
        print(count)
        a, b = bridges[i]
        if find(a) != find(b):
            count -= size[find(a)] * size[find(b)]
            unite(a, b)

if __name__ == '__main__':
    main()