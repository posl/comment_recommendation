def solve(n, a):
    ans = 0
    for i in range(1, n + 1):
        ans ^= i
    for i in range(4 * n - 1):
        ans ^= a[i]
    return ans
