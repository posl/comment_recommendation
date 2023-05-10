def solve():
    N, K = map(int, input().split())
    if K == 1:
        print(N + 1)
        return
    if K == N + 1:
        print(1)
        return
    MOD = 10 ** 9 + 7
    def modpow(a, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return modpow(a * a % MOD, n // 2)
        else:
            return a * modpow(a, n - 1) % MOD
    def modinv(a):
        return modpow(a, MOD - 2)
    def modcomb(n, r):
        if n < 0 or r < 0 or n < r:
            return 0
        return fact[n] * modinv(fact[r]) * modinv(fact[n - r]) % MOD
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    ans = 0
    for i in range(min(N, K - 1) + 1):
        ans += modcomb(N, i) * modcomb(N - 1, i) % MOD
        ans %= MOD
    print(ans)
solve()

if __name__ == '__main__':
    solve()