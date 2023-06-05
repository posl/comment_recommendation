def main():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0:
        print(0)
        return
    n = (2 * y - x) // 3
    m = (2 * x - y) // 3
    if n < 0 or m < 0:
        print(0)
        return
    N = n + m
    M = min(n, m)
    MOD = 10 ** 9 + 7
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (N + 1)
    inv[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N - 1, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % MOD
    def nCk(n, k):
        return fact[n] * inv[k] % MOD * inv[n - k] % MOD
    print(nCk(N, M))
