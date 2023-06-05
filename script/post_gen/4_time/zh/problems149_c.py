Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    m = int(n**0.5) + 1
    for i in range(3,m,2):
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
Suggestion 2

def isPrime(num):
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
Suggestion 3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
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
Suggestion 5

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True

x = int(input())
while True:
    if isPrime(x):
        print(x)
        exit()
    x += 1

=======
Suggestion 6

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2
    return True

n = int(input())
while not is_prime(n):
    n += 1
print(n)

=======
Suggestion 7

def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        else:
            i += 2
    return True

=======
Suggestion 8

def is_prime(n):
    if n == 2:
        return True
    elif n < 2 or n%2 == 0:
        return False
    else:
        i = 3
        while i <= n**0.5:
            if n%i == 0:
                return False
            i += 2
        return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    else:
        x += 1

=======
Suggestion 9

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

X = int(input())
while not is_prime(X):
    X += 1
print(X)

=======
Suggestion 10

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)
