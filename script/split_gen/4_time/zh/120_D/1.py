def main():
    n, m = map(int, input().split())
    a = [0] * (m + 1)
    b = [0] * (m + 1)
    for i in range(1, m + 1):
        a[i], b[i] = map(int, input().split())
    ans = [0] * (m + 1)
    uf = UnionFind(n + 1)
    cur = n * (n - 1) // 2
    for i in range(m, 0, -1):
        ans[i] = cur
        if uf.find(a[i]) != uf.find(b[i]):
            cur -= uf.size(a[i]) * uf.size(b[i])
            uf.union(a[i], b[i])
    for i in range(1, m + 1):
        print(ans[i])
