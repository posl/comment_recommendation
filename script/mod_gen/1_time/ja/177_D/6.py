def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    uf = UnionFind(n)
    for a, b in edges:
        uf.unite(a - 1, b - 1)
    print(uf.group_count)

if __name__ == '__main__':
    main()