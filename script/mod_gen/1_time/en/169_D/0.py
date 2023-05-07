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
for i in set(prime_factorize(n)):
    j = 1
    while n % (i ** j) == 0:
        n //= (i ** j)
        j += 1
    ans += j - 1
print(ans)

if __name__ == '__main__':
    prime_factorize()