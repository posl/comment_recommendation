def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    uf = UnionFind(N)
    for i in range(1, M):
        a, b = AB[i]
        a -= 1
        b -= 1
        if uf.same(a, b):
            ans[i] = ans[i - 1]
        else:
            ans[i] = ans[i - 1] - uf.size(a) * uf.size(b)
            uf.unite(a, b)
    for i in range(M - 1, -1, -1):
        print(ans[i])
