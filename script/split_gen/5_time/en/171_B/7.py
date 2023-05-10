def solve(N, K, p):
    p.sort()
    return sum(p[:K])
