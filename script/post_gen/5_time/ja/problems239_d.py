Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(a, b, c, d):
    for i in range(a, b+1):
        for j in range(c, d+1):
            if is_prime(i+j):
                return 'Takahashi'
    return 'Aoki'

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True

a, b, c, d = map(int, input().split())
for i in range(b+1):
    if a <= i <= b:
        if c <= i <= d:
            if is_prime(i + i):
                print("Aoki")
                exit()
        else:
            if is_prime(i + i):
                print("Aoki")
                exit()
    else:
        break
print("Takahashi")

=======
Suggestion 3

def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True

=======
Suggestion 4

def is_prime(n):
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
Suggestion 5

def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if not n % k:
            return False
    return True

a, b, c, d = map(int, input().split())
for i in range(100):
    if a <= c + i <= b and is_prime(c + i):
        print('Aoki')
        exit()
    if c <= a + i <= d and is_prime(a + i):
        print('Takahashi')
        exit()

=======
Suggestion 6

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if not n & 1: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True

a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    if is_prime(i):
        for j in range(c, d+1):
            if is_prime(j):
                if i + j == 5:
                    print("Aoki")
                    exit()
print("Takahashi")

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
    else:
        for k in range(2,n):
            if n % k == 0:
                return False
        return True

=======
Suggestion 8

def checkPrime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, int(x ** 0.5 + 1), 2):
        if x % i == 0:
            return False

    return True

=======
Suggestion 9

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

A,B,C,D = map(int,input().split())

=======
Suggestion 10

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
