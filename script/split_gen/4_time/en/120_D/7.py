def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab = ab[::-1]
    uf = UnionFind(n)
    ans = [0] * m
    ans[0] = n * (n - 1) // 2
    for i in range(m - 1):
        a, b = ab[i + 1]
        ans[i + 1] = ans[i]
        if uf.same(a - 1, b - 1):
            continue
        ans[i + 1] -= uf.size(a - 1) * uf.size(b - 1)
        uf.union(a - 1, b - 1)
    print(*ans[::-1], sep="\n")
