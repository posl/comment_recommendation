def solve(n, k):
    ans = 0
    while n > 0:
        n //= k
        ans += 1
    return ans
