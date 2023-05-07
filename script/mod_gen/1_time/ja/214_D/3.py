def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    ans = 0
    uf = UnionFind(n)
    for w, u, v in edges:
        ans += w * uf.size(u) * uf.size(v)
        uf.union(u, v)
    print(ans)

if __name__ == '__main__':
    main()