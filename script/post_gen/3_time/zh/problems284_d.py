Synthesizing 10/10 solutions

=======
Suggestion 1

def isPrime(num):
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False
    i = 5
    j = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += j
        j = 6 - j
    return True

=======
Suggestion 2

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

=======
Suggestion 3

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        return True

=======
Suggestion 4

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True

=======
Suggestion 5

def isPrime(num):
    if num == 2:
        return True
    if num == 3:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

=======
Suggestion 6

def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

=======
Suggestion 7

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 8

def isPrime(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return False
        return True

=======
Suggestion 9

def findPrime(n):
    prime = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            prime.append(i)
    return prime

=======
Suggestion 10

def isPrime(n):
    if n <= 1:
        return 0
    if n == 2 or n == 3:
        return 1
    if n % 6 != 1 and n % 6 != 5:
        return 0
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return 0
        i += 6
    return 1
