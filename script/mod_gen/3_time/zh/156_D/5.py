def solve(n, a, b):
    MOD = 10 ** 9 + 7
    # 1. nCkを求める
    # 2. nCkから、aCkとbCkを引く
    # 3. 2で求めた値をnCkから引く
    # 4. 3で求めた値をMODで割る
    def comb(n, k):
        x, y = 1, 1
        for i in range(k):
            x *= n - i
            y *= i + 1
            x %= MOD
            y %= MOD
        return x * pow(y, MOD - 2, MOD)
    ans = pow(2, n, MOD) - comb(n, a) - comb(n, b)
    return ans % MOD
n, a, b = map(int, input().split())
print(solve(n, a, b))
