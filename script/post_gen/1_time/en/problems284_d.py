Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return pow(2, n - 1, n) == 1

=======
Suggestion 2

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

=======
Suggestion 3

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

=======
Suggestion 4

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

=======
Suggestion 5

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

=======
Suggestion 6

def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

=======
Suggestion 8

def isprime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 9

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 10

def get_primes(n):
    is_prime = [True for i in range(n + 1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
