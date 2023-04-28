Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

X = int(input())
while not is_prime(X):
    X += 1
print(X)

I'm not sure if this is the best solution, but it's pretty fast.

import sys
import math

=======
Suggestion 2

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return pow(2, n-1, n) == 1

X = int(input())
while True:
    if is_prime(X):
        print(X)
        break
    X += 1

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

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return pow(2, n-1, n) == 1

=======
Suggestion 5

def is_prime(n):
    if n < 2:
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
Suggestion 6

def is_prime(n):
    if n == 2: return True
    if n < 2 or n%2 == 0: return False
    return all(n%i for i in range(3, int(n**0.5)+1, 2))

x = int(input())
while not is_prime(x):
    x += 1
print(x)

=======
Suggestion 7

def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

=======
Suggestion 8

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

X = int(input())

while True:
    if is_prime(X):
        print(X)
        break
    X += 1

Related

=======
Suggestion 9

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

X = int(input())
while True:
    if is_prime(X):
        print(X)
        break
    X += 1

=======
Suggestion 10

def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    x += 1
