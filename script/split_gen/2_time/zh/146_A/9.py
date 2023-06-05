def main():
    X, Y = map(int, input().split())
    mod = 10**9 + 7
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (2 * Y - X) // 3
    m = (2 * X - Y) // 3
    if n < 0 or m < 0:
        print(0)
        return
    N = n + m
    M = min(n, m)
    fac = [1] * (N + 1)
    for i in range(1, N + 1):
        fac[i] = fac[i - 1] * i % mod
    inv = [1] * (N + 1)
    inv[N] = pow(fac[N], mod - 2, mod)
    for i in range(N - 1, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % mod
    print(fac[N] * inv[M] * inv[N - M] % mod)
