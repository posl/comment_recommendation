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
d = {}
for i in range(1, n + 1):
    for j in prime_factorize(i):
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
a = 0
b = 0
c = 0
d = 0
e = 0
for i in d.values():
    if i >= 74:
        a += 1
    if i >= 24:
        b += 1
    if i >= 14:
        c += 1
    if i >= 4:
        d += 1
    if i >= 2:
        e += 1
print(a + b * (e - 1) + c * (d - 1) + d * (d - 1) * (e - 2) // 2)
