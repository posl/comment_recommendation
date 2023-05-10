def prime_factorize(n):
    from math import sqrt
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    f = 3
    while f <= sqrt(n):
        if n % f == 0:
            prime_factors.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime_factors.append(n)
    return prime_factors
n = int(input())
d = {}
for i in range(1,n+1):
    for j in prime_factorize(i):
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
cnt = 0
for i in d:
    if d[i] >= 74:
        cnt += 1
    for j in d:
        if i != j and d[i] >= 24 and d[j] >= 2:
            cnt += 1
        if i != j and d[i] >= 14 and d[j] >= 4:
            cnt += 1
        if i != j and d[i] >= 4 and d[j] >= 4 and i < j:
            cnt += 1
        for k in d:
            if i != j and j != k and k != i and d[i] >= 2 and d[j] >= 4 and d[k] >= 4:
                cnt += 1
print(cnt)
