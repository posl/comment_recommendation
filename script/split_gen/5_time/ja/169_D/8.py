def prime_factorize(n):
    prime_factor = []
    while n % 2 == 0:
        prime_factor.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            prime_factor.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime_factor.append(n)
    return prime_factor
n = int(input())
prime_list = prime_factorize(n)
prime_set = set(prime_list)
ans = 0
for p in prime_set:
    e = prime_list.count(p)
    tmp = 1
    while e >= tmp:
        e -= tmp
        tmp += 1
        ans += 1
print(ans)
