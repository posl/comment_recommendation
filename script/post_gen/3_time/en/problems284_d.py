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

T = int(input())
for i in range(T):
    N = int(input())
    p = prime_factorize(N)
    print(p[0], p[1])

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

t = int(input())
for i in range(0,t):
    n = int(input())
    p = prime_factors(n)
    q = int(n/(p[0]*p[0]))
    print(p[0],q)

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

def get_prime_factors(n):
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

=======
Suggestion 5

def primeFactors(n): 
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print(2), 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print(i), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print(n) 

t = int(input())
for i in range(t):
    n = int(input())
    primeFactors(n)

=======
Suggestion 6

def primeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

=======
Suggestion 8

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False

    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2

    return True

=======
Suggestion 9

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        p = 1
        q = 1
        for j in range(2, int(N**(1/3))+1):
            if N%j == 0:
                p = j
                q = N//j
                break
        print(p, q)

=======
Suggestion 10

def get_primes(n):
    primes = []
    for i in range(2, n+1):
        if all([i % p != 0 for p in primes]):
            primes.append(i)
    return primes
