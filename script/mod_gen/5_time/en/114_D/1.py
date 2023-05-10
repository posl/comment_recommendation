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
for i in range(1, n+1):
    for j in prime_factorize(i):
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
ans = 0
for i in d.values():
    if i >= 74:
        ans += 1
for i in d.values():
    for j in d.values():
        if i != j and i >= 24 and j >= 2:
            ans += 1
for i in d.values():
    for j in d.values():
        if i != j and i >= 14 and j >= 4:
            ans += 1
for i in d.values():
    for j in d.values():
        if i != j and i >= 4 and j >= 4:
            for k in d.values():
                if k != i and k != j and k >= 2:
                    ans += 1
print(ans)

if __name__ == '__main__':
    prime_factorize()