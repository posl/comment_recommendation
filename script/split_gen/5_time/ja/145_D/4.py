def solve():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        return 0
    if X > Y:
        X, Y = Y, X
    if Y > 2 * X:
        return 0
    if X == Y:
        return 2 ** X % MOD
    x = (2 * X - Y) // 3
    y = (2 * Y - X) // 3
    ans = 1
    for i in range(1, x + 1):
        ans = ans * (x + y - i + 1) * pow(i, MOD - 2, MOD) % MOD
    return ans
MOD = 10 ** 9 + 7
print(solve())
