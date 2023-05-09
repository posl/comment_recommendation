def solve():
    N, K = map(int, input().split())
    MOD = 10**9+7
    def comb(n, r, mod=MOD):
        if n < 0 or r < 0 or n < r:
            return 0
        r = min(r, n - r)
        if r == 0:
            return 1
        if r == 1:
            return n % mod
        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]
        for p in range(2, r + 1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p - 1, r, p):
                    numerator[k - offset] //= pivot
                    denominator[k] //= pivot
        result = 1
        for k in range(r):
            if numerator[k] > 1:
                result = (result * numerator[k]) % mod
        return result
    ans = 0
    for i in range(K, N+2):
        ans += comb(N+1, i)
        ans %= MOD
    print(ans)
