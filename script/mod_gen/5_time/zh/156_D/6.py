def solve(n, a, b):
    MOD = 10**9 + 7
    ans = pow(n, 2, MOD)
    ans -= pow(n - a, 2, MOD)
    ans -= pow(n - b, 2, MOD)
    ans += pow(n - a - b, 2, MOD)
    ans %= MOD
    ans = ans * (n - 2) % MOD
    ans = ans * (n - 1) % MOD
    ans = ans * 500000004 % MOD
    return ans
n, a, b = map(int, input().split())
print(solve(n, a, b))
