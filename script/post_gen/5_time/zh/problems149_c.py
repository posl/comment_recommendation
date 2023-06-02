Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

=======
Suggestion 2

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

=======
Suggestion 3

def isPrime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i*i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    x += 1

=======
Suggestion 4

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)

=======
Suggestion 5

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2): # 从3开始，每次加2
        if n%i == 0:
            return False
    return True

=======
Suggestion 6

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1

=======
Suggestion 7

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


X = int(input())
while not is_prime(X):
    X += 1
print(X)

=======
Suggestion 8

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or not n % 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True

=======
Suggestion 9

def is_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2

    return True

=======
Suggestion 10

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
X = int(input())
while True:
    if isPrime(X):
        print(X)
        break
    else:
        X += 1
