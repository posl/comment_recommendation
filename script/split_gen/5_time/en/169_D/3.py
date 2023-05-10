def factorize(n):
    fct = []
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct
n = int(input())
f = factorize(n)
ans = 0
for i in range(len(f)):
    c = 0
    while f[i][1] >= c:
        f[i] = (f[i][0], f[i][1] - c)
        c += 1
        ans += 1
print(ans - 1)
