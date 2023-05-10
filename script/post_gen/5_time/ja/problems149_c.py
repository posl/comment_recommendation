Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
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

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2): # 3~nの平方根まで2刻みで繰り返し
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
Suggestion 3

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        #print(i)
        if n % i == 0:
            return False
    return True

x = int(input())

while True:
    #print(x)
    if is_prime(x):
        print(x)
        exit()
    x += 1

=======
Suggestion 4

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
Suggestion 5

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        exit()
    x += 1

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        exit()
    x += 1

=======
Suggestion 7

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

x = int(input())

while True:
    if is_prime(x):
        print(x)
        break
    x += 1

=======
Suggestion 8

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
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

def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1

=======
Suggestion 10

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
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
