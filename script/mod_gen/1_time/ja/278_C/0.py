def main():
    n, q = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            uf.union(a - 1, b - 1)
        elif t == 2:
            if uf.same(a - 1, b - 1):
                uf.union(a - 1, b - 1)
                uf.union(b - 1, a - 1)
        else:
            if uf.same(a - 1, b - 1):
                print("Yes")
            else:
                print("No")

if __name__ == '__main__':
    main()