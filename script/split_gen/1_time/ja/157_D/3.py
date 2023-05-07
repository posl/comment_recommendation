def main():
    n, m, k = map(int, input().split())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    c = [0] * (n + 1)
    d = [0] * (n + 1)
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    for i in range(k):
        c[i], d[i] = map(int, input().split())
    for i in range(m):
        a[i] -= 1
        b[i] -= 1
    for i in range(k):
        c[i] -= 1
        d[i] -= 1
    uf = UnionFind(n)
    for i in range(m):
        uf.union(a[i], b[i])
    for i in range(k):
        uf.union(c[i], d[i])
    ans = [0] * n
    for i in range(n):
        ans[i] = uf.size(i) - uf.size_tree(i) - 1
    print(*ans)
