def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    uf = UnionFind(n)
    ans = [0] * m
    ans[m-1] = n * (n - 1) // 2
    for i in range(m-1, 0, -1):
        a, b = ab[i]
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i-1] = ans[i]
        else:
            ans[i-1] = ans[i] - uf.size(a) * uf.size(b)
        uf.union(a, b)
    for i in range(m):
        print(ans[i])

if __name__ == '__main__':
    main()