def main():
    n, q = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            uf.union(a, b)
        elif t == 2:
            uf.unite(a, b)
        else:
            print('Yes' if uf.same(a, b) else 'No')
