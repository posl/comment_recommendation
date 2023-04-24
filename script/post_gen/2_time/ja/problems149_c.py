Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

=======
Suggestion 2

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return not any(n % i == 0 for i in range(3, int(n**0.5)+1, 2))

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    else:
        x += 1

=======
Suggestion 3

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

=======
Suggestion 4

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

X = int(input())
while True:
    if is_prime(X):
        print(X)
        break
    X += 1

=======
Suggestion 5

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

=======
Suggestion 6

def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
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

def isPrime(n):
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
Suggestion 8

def prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 9

def is_prime(n):
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

=======
Suggestion 10

def prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    return prime(x-2)

x = int(input())

while True:
    if prime(x):
        print(x)
        break
    x += 1
