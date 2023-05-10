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
a = prime_factorize(N)
a = list(set(a))
a.sort()
a.reverse()
ans = 0
for i in range(len(a)):
    tmp = N
    while tmp % a[i] == 0:
        tmp //= a[i]
    N = tmp
    ans += 1
print(ans)
