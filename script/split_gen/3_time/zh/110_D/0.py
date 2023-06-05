def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
n, m = map(int, input().split())
mod = 10**9 + 7
ans = 1
for x in prime_factorize(m):
    y = 0
    while m % x == 0:
        m //= x
        y += 1
    ans *= y + n - 1
    ans %= mod
print(ans)
