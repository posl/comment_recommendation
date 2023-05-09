def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res
n, m = map(int, input().split())
mod = 10 ** 9 + 7
ans = 1
for i in range(2, int(m ** 0.5) + 1):
    if m % i == 0:
        cnt = 0
        while m % i == 0:
            m //= i
            cnt += 1
        ans *= modpow(cnt + n - 1, n - 1, mod)
        ans %= mod
