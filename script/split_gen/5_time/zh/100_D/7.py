def solve():
    n, m = map(int, input().split())
    x, y, z = [], [], []
    for i in range(n):
        xi, yi, zi = map(int, input().split())
        x.append(xi)
        y.append(yi)
        z.append(zi)
    ans = 0
    for i in range(2 ** 3):
        d = []
        for j in range(n):
            d.append(x[j] * ((i >> 0) & 1) + y[j] * ((i >> 1) & 1) + z[j] * ((i >> 2) & 1))
        d.sort(reverse=True)
        ans = max(ans, sum(d[:m]))
    print(ans)
solve()
