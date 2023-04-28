Synthesizing 10/10 solutions

=======
Suggestion 1

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

t = int(input())
for i in range(t):
    n = int(input())
    a = prime_factorize(n)
    print(a[0], a[1])

=======
Suggestion 2

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

t=int(input())
for i in range(t):
    n=int(input())
    x=prime_factors(n)
    a=x[0]
    b=x[1]
    print(a,b)

=======
Suggestion 3

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

T = int(input())
for i in range(T):
    N = int(input())
    prime = prime_factors(N)
    p = prime[0]
    q = prime[1]
    print(p, q)

=======
Suggestion 4

def prime_factorization(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

T = int(input())
for _ in range(T):
    N = int(input())
    table = prime_factorization(N)
    p = table[0]
    q = table[1]
    print(p, q)

=======
Suggestion 5

def primefactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

T = int(input())
for i in range(T):
    N = int(input())
    factors = primefactors(N)
    if len(factors) == 2:
        print(factors[0], factors[1])
    else:
        print(factors[0], factors[1]*factors[2])

=======
Suggestion 6

def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

t = int(input())
for i in range(t):
    n = int(input())
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            if is_prime(n // j):
                print(str(j) + " " + str(n // j))
                break

=======
Suggestion 7

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

=======
Suggestion 8

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
Suggestion 9

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

=======
Suggestion 10

def findPrimeFactors(n):
    factors = []
    i = 2
    while i*i <= n:
        if n%i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

t = int(input())
for _ in range(t):
    n = int(input())
    factors = findPrimeFactors(n)
    if len(set(factors)) == 2:
        p = factors[0]
        q = factors[1]
        print(p, q)
    else:
        print(0, 0)
