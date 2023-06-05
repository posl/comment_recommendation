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
MOD = 10**9 + 7
ans = 1
for i in range(1, m + 1):
    cnt = 0
    for p in prime_factorize(i):
        cnt += 1
    ans *= pow(cnt, n, MOD)
    ans %= MOD
print(ans)
