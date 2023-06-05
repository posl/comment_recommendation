def solve(n):
    k = 1
    while k * k < n:
        k += 1
    k -= 1
    if k * k == n:
        return 2 * k - 2
    if n - k * k <= k:
        return 2 * k - 1
    return 2 * k
