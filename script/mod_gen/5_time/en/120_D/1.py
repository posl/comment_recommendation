def main():
    n, m = map(int, input().split())
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    for i in range(1, m + 1):
        a[i], b[i] = map(int, input().split())
    uf = UnionFind(n + 1)
    ans = [0] * (m + 1)
    ans[m] = n * (n - 1) // 2
    for i in range(m, 0, -1):
        ans[i - 1] = ans[i]
        if uf.same(a[i], b[i]):
            continue
        ans[i - 1] -= uf.size(a[i]) * uf.size(b[i])
        uf.unite(a[i], b[i])
    for i in range(1, m + 1):
        print(ans[i])

if __name__ == '__main__':
    main()