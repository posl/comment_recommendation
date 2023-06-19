def main():
    n, m = map(int, input().split())
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    for i in range(1, n):
        a[i], b[i] = map(int, input().split())
    ans = n * (n - 1) // 2
    par = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
    def same(x, y):
        return find(x) == find(y)
    for i in range(1, n):
        unite(a[i], b[i])
    for i in range(m):
        a, b = map(int, input().split())
        if same(a, b):
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()