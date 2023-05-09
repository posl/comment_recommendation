def solve(a: int, n: int):
    if n < a:
        return -1
    x = 1
    ans = 0
    while x < n:
        x *= a
        ans += 1
    if x > n:
        ans -= 1
        x //= a
    if x == n:
        return ans
    if x == 1:
        return -1
    ans += (n - x) // (x // a) + 1
    return ans
