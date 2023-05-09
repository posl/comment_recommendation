def f(n, d):
    if n < 10 ** d:
        return n
    else:
        return 9 * 10 ** (d - 1) + f(n - 9 * 10 ** (d - 1), d + 1)
n = int(input())
d = 1
ans = 0
while 10 ** d <= n:
    ans += f(10 ** d - 1, d)
    d += 1
ans += f(n, d)
print(ans % 998244353)
