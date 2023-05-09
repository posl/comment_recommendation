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
count = 0
for n in range(1, N + 1):
    if n % 2 != 0:
        if len(prime_factorize(n)) == 8:
            count += 1
print(count)
