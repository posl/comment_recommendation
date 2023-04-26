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

while True:
    if is_prime(X):
        print(X)
        break
    X += 1

=======
Suggestion 2

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
Suggestion 3

def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    else:
        x += 1

=======
Suggestion 4

def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
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

=======
Suggestion 5

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    return pow(2, x-1, x) == 1

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
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
Suggestion 7

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 8

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1

=======
Suggestion 9

def prime(n):
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
Suggestion 10

def prime_check(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

X = int(input())
while True:
    if prime_check(X):
        print(X)
        break
    X += 1
