Synthesizing 10/10 solutions

=======
Suggestion 1

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

x = int(input())

=======
Suggestion 2

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5)+1, 2):
        if x % i == 0:
            return False
    return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)

=======
Suggestion 3

def isPrime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

X = int(input())

=======
Suggestion 4

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False

    i = 3
    while i <= x**0.5:
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
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

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
    X += 1

=======
Suggestion 7

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True

x = int(input())
while not is_prime(x):
    x += 1
print(x)

=======
Suggestion 8

def is_prime(n):
    if n <= 1:
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
Suggestion 9

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
 
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
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
Suggestion 10

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0: # 偶数はあらかじめ除外
        return False
    for i in range(3, int(n**0.5)+1, 2): # 3からnの平方根までの奇数で割り切れるかチェック
        if n % i == 0:
            return False
    return True

x = int(input())
while True:
    if is_prime(x):
        print(x)
        break
    x += 1
