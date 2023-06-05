def solve(n, k, ps):
    ps = sorted(ps)
    s = sum(ps[-k:])
    return (s+k)/2
