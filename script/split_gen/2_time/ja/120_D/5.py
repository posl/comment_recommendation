def main():
    n, m = map(int, input().split())
    a, b = zip(*[map(int, input().split()) for _ in range(m)])
    a = [a_ - 1 for a_ in a]
    b = [b_ - 1 for b_ in b]
    # 連結成分
    uf = UnionFind(n)
    for i in range(m):
        uf.union(a[i], b[i])
    # 連結成分ごとに島の数を数える
    islands = [0] * n
    for i in range(n):
        islands[uf.root(i)] += 1
    # 連結成分の島の数の和を計算する
    sums = [0] * n
    for i in range(n):
        sums[uf.root(i)] += islands[i]
    # 連結成分ごとに不便さを計算する
    ans = [0] * m
    for i in range(m - 1, -1, -1):
        ans[i] = sums[uf.root(a[i])] * sums[uf.root(b[i])]
        sums[uf.root(a[i])] = 0
        sums[uf.root(b[i])] = 0
    # 累積和を計算する
    for i in range(1, m):
        ans[i] += ans[i - 1]
    for i in range(m):
        print(ans[i])
