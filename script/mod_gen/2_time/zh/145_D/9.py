def main():
    X, Y = map(int, input().split())
    mod = 10**9 + 7
    if (X + Y) % 3 != 0:
        print(0)
        return
    n = (2 * X - Y) // 3
    m = (2 * Y - X) // 3
    if n < 0 or m < 0:
        print(0)
        return
    N = n + m
    if N > n:
        n, m = N - n, n
    fac = [1] * (n + 1)
    for i in range(2, n + 1):
        fac[i] = fac[i - 1] * i % mod
    inv = [1] * (n + 1)
    inv[n] = pow(fac[n], mod - 2, mod)
    for i in range(n - 1, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % mod
    print(fac[N] * inv[n] * inv[m] % mod)

if __name__ == '__main__':
    main()