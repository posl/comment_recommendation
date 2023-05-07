def main():
    N, M = [int(x) for x in input().split()]
    bridges = [tuple(int(x) for x in input().split()) for i in range(M)]
    bridges.reverse()
    # Union-Find Tree
    root = [i for i in range(N + 1)]
    size = [1 for i in range(N + 1)]
    def find(x):
        if root[x] == x:
            return x
        else:
            root[x] = find(root[x])
            return root[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if size[x] < size[y]:
            x, y = y, x
        root[y] = x
        size[x] += size[y]
        return True
    # 結合前の不便さ
    inconvenience = sum((size[i] * (size[i] - 1)) // 2 for i in range(1, N + 1))
    print(inconvenience)
    for a, b in bridges:
        if unite(a, b):
            inconvenience -= (size[find(a)] * (size[find(a)] - 1)) // 2
            inconvenience -= (size[find(b)] * (size[find(b)] - 1)) // 2
        print(inconvenience)

if __name__ == '__main__':
    main()