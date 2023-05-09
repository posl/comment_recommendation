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
for _ in range(t):
    n = int(input())
    a = prime_factorize(n)
    p = a[0]
    for i in range(1, len(a)):
        if a[i] != p:
            q = a[i]
            break
    print(p, q)

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

T = int(input())
for i in range(T):
    N = int(input())
    factors = prime_factors(N)
    if len(factors) == 3:
        print(factors[0], factors[1]*factors[2])
    else:
        print(factors[0]*factors[1], factors[2])

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

t = int(input())
for i in range(t):
    n = int(input())
    factors = prime_factors(n)
    p = factors[0]
    q = factors[1]
    print(p, q)

=======
Suggestion 4

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

for _ in range(int(input())):
    n = int(input())
    factors = prime_factors(n)
    p = factors[0]
    q = factors[1]
    print(p, q)

=======
Suggestion 5

def primeFactors(n):
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
    factors = primeFactors(N)
    p = factors[0]
    q = factors[1]
    print(p,q)

=======
Suggestion 6

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

=======
Suggestion 7

def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(int(i))
    if n > 1:
        factors.append(int(n))
    return factors

T = int(input())
for i in range(T):
    N = int(input())
    factors = primeFactors(N)
    p = factors[0]
    q = factors[1]
    print(p,q)

=======
Suggestion 8

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    i = 3
    while i*i <= n:
        if n % i ==0:
            return False
        i += 2
    return True

=======
Suggestion 9

def get_factors(n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

=======
Suggestion 10

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1): #int(n**0.5)+1
        if n % i == 0:
            return False
    return True
