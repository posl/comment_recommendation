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
t=int(input())
for i in range(t):
    n=int(input())
    a=prime_factorize(n)
    print(a[0],a[1])

if __name__ == '__main__':
    prime_factorize()