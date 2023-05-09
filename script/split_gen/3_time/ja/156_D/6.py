def main():
    n, a, b = map(int, input().split())
    MOD = 10**9 + 7
    x = pow(2, n, MOD) - 1
    y = 1
    for i in range(1, a + 1):
        y = y * (n - i + 1) * pow(i, MOD - 2, MOD) % MOD
    z = 1
    for i in range(1, b + 1):
        z = z * (n - i + 1) * pow(i, MOD - 2, MOD) % MOD
    print((x - y - z) % MOD)
