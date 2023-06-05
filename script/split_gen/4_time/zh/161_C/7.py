def solve(n, k):
    while True:
        if n < k:
            return min(n, abs(n-k))
        else:
            n %= k
    return n
