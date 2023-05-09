def solve(a, b, k):
    if b <= k:
        return 0
    if a >= k:
        return 1
    if a < k and b > k:
        return 2
    return 0
