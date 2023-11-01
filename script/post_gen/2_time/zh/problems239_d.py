Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 ==0:
        return False
    else:
        for i i

=======
Suggestion 2

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1): #int(n**0.5)+1 为了提高效率
        if n % i == 0:
            return False

=======
Suggestion 3

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return F

=======
Suggestion 5

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    i = 3
    while i * i <= n:

=======
Suggestion 7

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return F

=======
Suggestion 8

def isPrime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    i = 3
    while i <= num ** 0.5:
        if num %

=======
Suggestion 9

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1, 2):
        if n % i

=======
Suggestion 10

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True
