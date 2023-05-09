def solve(n):
    ans = 0
    for i in range(1, len(str(n))):
        ans += 9 * i * pow(10, i - 1, 998244353)
    ans %= 998244353
    ans += (n - pow(10, len(str(n)) - 1) + 1) * len(str(n))
    ans %= 998244353
    return ans
