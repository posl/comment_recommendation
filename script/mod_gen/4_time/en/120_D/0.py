def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.reverse()
    B.reverse()
    ans = N * (N - 1) // 2
    uf = UnionFind(N)
    anss = []
    for i in range(M):
        anss.append(ans)
        a = A.pop()
        b = B.pop()
        if uf.same(a - 1, b - 1):
            continue
        ans -= uf.size(a - 1) * uf.size(b - 1)
        uf.unite(a - 1, b - 1)
    anss.reverse()
    for i in range(M):
        print(anss[i])

if __name__ == '__main__':
    main()