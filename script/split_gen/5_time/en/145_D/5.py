def solve():
    X, Y = map(int, input().split())
    mod = 10**9 + 7
    if (X + Y) % 3 != 0:
        return 0
    if (2 * X - Y) % 3 != 0:
        return 0
    if (2 * Y - X) % 3 != 0:
        return 0
    a = (2 * X - Y) // 3
    b = (2 * Y - X) // 3
    if a < 0 or b < 0:
        return 0
    n = a + b
    r = a
    ans = 1
    for i in range(r):
        ans = (ans * (n - i)) % mod
        ans = (ans * pow(i + 1, mod - 2, mod)) % mod
    return ans
