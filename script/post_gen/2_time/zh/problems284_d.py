Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True

=======
Suggestion 2

def isPrime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

=======
Suggestion 3

def prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 4

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n ** 0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

=======
Suggestion 5

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n%2 == 0:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1+max_div, 2):
        if n%i == 0:
            return False
    return True

=======
Suggestion 6

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

=======
Suggestion 7

def isPrime(num):
    if num == 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

=======
Suggestion 8

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 9

def isPrime(n):
    if n <= 1:
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
Suggestion 10

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
