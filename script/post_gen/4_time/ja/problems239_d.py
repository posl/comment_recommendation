Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True

A, B, C, D = map(int, input().split())

for i in range(B+1, 100):
    if is_prime(i):
        B = i
        break

for i in range(C-1, 0, -1):
    if is_prime(i):
        C = i
        break

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    if is_prime(i):
        for j in range(c, d+1):
            if is_prime(j):
                if i+j == 1:
                    print("Aoki")
                    exit()
print("Takahashi")

=======
Suggestion 3

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False
    i = 5
    j = 2
    while i * i <= n:
        if n % i == 0: return False
        i += j
        j = 6 - j
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

a,b,c,d = map(int,input().split())
for i in range(100):
    if is_prime(a+c+i):
        print("Takahashi")
        exit()
    elif is_prime(b+d+i):
        print("Aoki")
        exit()

=======
Suggestion 5

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())
for i in range(100):
    if is_prime(A + i):
        print("Takahashi")
        exit()
    elif is_prime(C + i):
        print("Aoki")
        exit()

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

=======
Suggestion 7

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

A, B, C, D = map(int, input().split())
for i in range(B + 1, D + 1):
    if is_prime(i):
        print("Aoki")
        exit()
print("Takahashi")

=======
Suggestion 8

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if (n % 2) == 0:
        return False
    i = 3
    while i <= (n**0.5):
        if (n % i) == 0:
            return False
        i += 2
    return True

a,b,c,d = map(int,input().split())

for i in range(a,b+1):
    if isPrime(i):
        for j in range(c,d+1):
            if isPrime(j):
                if i+j == 0:
                    print("Aoki")
                    exit()
print("Takahashi")

=======
Suggestion 9

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    i = 3
    while i <= n**0.5:
        if n % i == 0:
            return False
        i += 2
    return True

a,b,c,d = map(int,input().split())
for i in range(a,b+1):
    for j in range(c,d+1):
        if is_prime(i+j):
            print("Aoki")
            exit()
print("Takahashi")

=======
Suggestion 10

def primecheck(n):
    if n == 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    else:
        return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    if primecheck(i):
        for j in range(c, d+1):
            if primecheck(j):
                if primecheck(i+j):
                    print("Aoki")
                    exit()
print("Takahashi")
