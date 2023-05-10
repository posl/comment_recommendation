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
n = int(input())
ans = 0
for i in range(2,n+1):
    a = prime_factorize(i)
    if len(a) == 2:
        if a[0] * a[1] ** 3 == i:
            ans += 1
print(ans)
