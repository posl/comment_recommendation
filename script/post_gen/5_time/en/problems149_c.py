Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)

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

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2

    return True

x = int(input())

while not is_prime(x):
    x += 1

print(x)

=======
Suggestion 4

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True

X = int(input())
while not is_prime(X):
    X += 1
print(X)

=======
Suggestion 5

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True

x = int(input())
while is_prime(x) == False:
    x += 1
print(x)

=======
Suggestion 6

def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True


x = int(input())
while True:
    if isPrime(x):
        print(x)
        break
    x += 1

=======
Suggestion 7

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5+1), 2):
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
Suggestion 8

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

x = int(input())
while not isPrime(x):
    x += 1
print(x)

=======
Suggestion 9

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    i = 3
    while i ** 2 <= num:
        if num % i == 0:
            return False
        i += 2

    return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)

=======
Suggestion 10

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1): #int(n**0.5)+1
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
