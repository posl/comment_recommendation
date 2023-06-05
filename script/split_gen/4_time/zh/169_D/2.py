def prime_factorize(n):
    # 素因数分解
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
a = prime_factorize(n)
b = list(set(a))
c = sorted(b)
ans = 0
for i in c:
    ans += a.count(i)
print(ans)
