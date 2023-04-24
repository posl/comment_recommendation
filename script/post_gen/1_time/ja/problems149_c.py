Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return not any(n % i == 0 for i in range(3, int(n ** 0.5) + 1, 2))

=======
Suggestion 2

def is_prime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

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
    if n < 2 or n % 2 == 0:
        return False
    return pow(2, n - 1, n) == 1

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
        return True

X = int(input())
while True:
    if is_prime(X):
        print(X)
        break
    else:
        X += 1

=======
Suggestion 5

def is_prime(x):
    if x == 1:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

x = int(input())

while True:
    if is_prime(x):
        print(x)
        break
    x += 1

=======
Suggestion 6

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1

=======
Suggestion 7

def isPrime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

x = int(input())

while not isPrime(x):
    x += 1

print(x)

import math

=======
Suggestion 8

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

=======
Suggestion 9

def isPrime(x):
    if x == 2:
        return True
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

=======
Suggestion 10

def main():
    X = int(input())
    for i in range(X, 100001):
        if is_prime(i):
            print(i)
            break
