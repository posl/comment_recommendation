Synthesizing 10/10 solutions

=======
Suggestion 1

def get_primes(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

=======
Suggestion 2

def is_prime(n):
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n%3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

=======
Suggestion 3

def solve(n):
    if n % 2 == 0:
        if n % 4 == 0:
            return int(n/4), 2
        else:
            return int(n/2), 2

    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            if n % (i**2) == 0:
                return int(n/(i**2)), i
            else:
                return n//i, i
    return n, 1

=======
Suggestion 4

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    x = 3
    while x * x <= n:
        if n % x == 0:
            return False
        x += 2
    return True

=======
Suggestion 5

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True

=======
Suggestion 6

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n ** 0.5) + 1
    for i in range(3, sqr, 2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 7

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

=======
Suggestion 8

def isPrime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    j = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += j
        j = 6 - j
    return True

=======
Suggestion 9

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        i = 3
        while i*i <= n:
            if n%i == 0:
                return False
            i += 2
        return True

=======
Suggestion 10

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True
