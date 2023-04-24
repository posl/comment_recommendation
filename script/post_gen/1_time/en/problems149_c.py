Synthesizing 10/10 solutions

=======
Suggestion 1

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

x = int(input())
while not isPrime(x):
    x += 1
print(x)

=======
Suggestion 2

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif not num & 1:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if not num % i:
            return False
    return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)

=======
Suggestion 3

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i+2
    return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1

=======
Suggestion 5

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
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
Suggestion 6

def isPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)

=======
Suggestion 8

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n :
        if n % i == 0:
            return False
        i += 2
    return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)

=======
Suggestion 9

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    else:
        x += 1

=======
Suggestion 10

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            return False
    return True

X = int(input())
while not isPrime(X):
    X += 1
print(X)
