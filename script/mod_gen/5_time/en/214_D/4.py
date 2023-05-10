def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u,v,w))
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    ans = 0
    for u, v, w in edges:
        ans += uf.size(u) * uf.size(v) * w
        uf.union(u, v)
    print(ans)

if __name__ == '__main__':
    main()