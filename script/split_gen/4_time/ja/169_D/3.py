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
N = int(input())
ans = 0
pf = prime_factorize(N)
for i in range(len(pf)):
    if i == 0:
        ans += 1
    elif pf[i] != pf[i-1]:
        ans += 1
print(ans)
