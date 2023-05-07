def f(n):
    if n < 10:
        return n
    else:
        l = len(str(n))
        return (9 * (l - 1) * pow(10, l - 2, MOD) + (n - pow(10, l - 1, MOD) + 1)) % MOD
n = int(input())
MOD = 998244353
ans = 0
for i in range(1, len(str(n)) + 1):
    m = pow(10, i, MOD) - 1
    ans += f(m)
    ans %= MOD
ans += f(n)
ans %= MOD
print(ans)
This code is written in Python 3.4.3.
Th

if __name__ == '__main__':
    f()