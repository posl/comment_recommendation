def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    ans = [0] * M
    ans[M - 1] = N * (N - 1) // 2
    uf = UnionFind(N)
    for i in range(M - 1, 0, -1):
        a = A[i] - 1
        b = B[i] - 1
        if uf.same(a, b):
            ans[i - 1] = ans[i]
        else:
            ans[i - 1] = ans[i] - uf.size(a) * uf.size(b)
            uf.unite(a, b)
    for i in range(M):
        print(ans[i])
