def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
T = int(input())
for i in range(T):
    N = int(input())
    N = N * 2
    primfac = primes(N)
    primfac = list(set(primfac))
    primfac.sort()
    print(primfac[0], primfac[1])

if __name__ == '__main__':
    primes()