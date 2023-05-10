def main():
    n, m = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(m)]
    bridges.reverse()
    uf = UnionFind(n)
    ans = [0] * m
    ans[m-1] = (n * (n-1)) // 2
    for i in range(m-1):
        a, b = bridges[i]
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i] = ans[i+1]
        else:
            ans[i] = ans[i+1] - uf.size(a) * uf.size(b)
            uf.unite(a, b)
    print(*ans[::-1], sep="\n")

if __name__ == '__main__':
    main()