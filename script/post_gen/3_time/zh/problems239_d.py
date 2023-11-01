Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 2 or n == 3:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:

=======
Suggestion 2

def isPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n <= 1:
        return False
    else:
        for i in range(3, i

=======
Suggestion 3

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(n**0.5)+1):

=======
Suggestion 4

def is_primes(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):

=======
Suggestion 5

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                retur

=======
Suggestion 6

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

=======
Suggestion 7

def is_prime(n):
    if n==1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:

=======
Suggestion 8

def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

=======
Suggestion 9

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 ==0:
        return False
    f

=======
Suggestion 10

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
