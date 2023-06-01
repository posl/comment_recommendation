Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        i = 3
        while i <= int(num ** 0.5) + 1:
            if num % i == 0:
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
Suggestion 2

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

=======
Suggestion 3

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
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
Suggestion 4

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+2, 2):
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
Suggestion 5

def IsPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i==0:
            return False
        i += 2
    return True

=======
Suggestion 6

def isPrime(n):
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
Suggestion 7

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
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
Suggestion 8

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

x = int(input())
while not isPrime(x):
    x += 1
print(x)

=======
Suggestion 9

def is_prime(x):
    for i in range(2, x):
        if (x % i == 0):
            return False
    return True

x = int(input())
while (not is_prime(x)):
    x += 1
print(x)

=======
Suggestion 10

def is_prime(n):
    if n == 2:
        return True
    if n<2 or n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)
