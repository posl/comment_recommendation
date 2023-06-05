def solve(n, k):
    return min(n % k, k - (n % k))
