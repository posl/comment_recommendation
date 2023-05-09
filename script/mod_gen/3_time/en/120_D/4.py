def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab.reverse()
    ans = [n * (n - 1) // 2]
    uf = UnionFind(n)
    for a, b in ab:
        a -= 1
        b -= 1
        ans.append(ans[-1] - uf.size(a) * uf.size(b))
        uf.unite(a, b)
    for a in ans[:-1][::-1]:
        print(a)

if __name__ == '__main__':
    main()