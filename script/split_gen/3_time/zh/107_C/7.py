def solve(n, k, xs):
    if k == 1:
        return 0
    if n == k:
        return xs[n - 1] - xs[0]
    res = 10 ** 9
    for i in range(0, n - k + 1):
        res = min(res, xs[i + k - 1] - xs[i] + min(abs(xs[i]), abs(xs[i + k - 1])))
    return res
