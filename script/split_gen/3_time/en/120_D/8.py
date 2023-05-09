def main():
    N, M = map(int, input().split())
    bridges = [tuple(map(int, input().split())) for _ in range(M)]
    bridges.reverse()
    ans = [0] * M
    ans[0] = N * (N - 1) // 2
    uf = UnionFind(N)
    for i, (a, b) in enumerate(bridges):
        if i == 0:
            continue
        ans[i] = ans[i - 1]
        if uf.same(a - 1, b - 1):
            continue
        ans[i] -= uf.size(a - 1) * uf.size(b - 1)
        uf.union(a - 1, b - 1)
    print('
'.join(map(str, ans[::-1])))
