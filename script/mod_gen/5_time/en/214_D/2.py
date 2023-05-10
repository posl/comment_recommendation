def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    ans = 0
    uf = UnionFind(N)
    for w, u, v in edges:
        ans += uf.size(u) * uf.size(v) * w
        uf.unite(u, v)
    print(ans)

if __name__ == '__main__':
    main()