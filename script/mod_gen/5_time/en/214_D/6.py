def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    edges.sort(key = lambda x: x[2])
    uf = UnionFind(n)
    ans = 0
    for a, b, c in edges:
        ans += uf.size(a) * uf.size(b) * c
        uf.union(a, b)
    print(ans)

if __name__ == '__main__':
    main()