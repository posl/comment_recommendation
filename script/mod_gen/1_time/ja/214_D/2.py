def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    tree = UnionFind(n)
    ans = 0
    for w, u, v in edges:
        size_u = tree.size(u)
        size_v = tree.size(v)
        ans += w * size_u * size_v
        tree.unite(u, v)
    print(ans)

if __name__ == '__main__':
    main()