def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ans = [0] * m
    ans[-1] = n * (n - 1) // 2
    uf = UnionFind(n)
    for i in range(m - 1, 0, -1):
        a, b = ab[i]
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i - 1] = ans[i]
        else:
            ans[i - 1] = ans[i] - uf.size(a) * uf.size(b)
            uf.union(a, b)
    print(*ans, sep='\n')
