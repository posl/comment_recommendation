def solve(n, x, xs):
    xs.sort()
    ds = []
    for i in range(n-1):
        ds.append(xs[i+1] - xs[i])
    ds.sort()
    if n == 1:
        return ds[0]
    else:
        return gcd(ds[0], ds[1])
