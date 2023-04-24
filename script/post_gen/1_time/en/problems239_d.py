Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(x):
    if x < 2: return False
    if x == 2: return True
    if x%2 == 0: return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0:
            return False
    return True

a,b,c,d = map(int, input().split())
for i in range(100):
    if a+i > b:
        print('Aoki')
        exit()
    if c+i > d:
        print('Takahashi')
        exit()
    if is_prime(a+i+c+i):
        print('Aoki')
        exit()
    if is_prime(a+i+c+i+1):
        print('Takahashi')
        exit()

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
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

a,b,c,d = map(int, input().split())

for i in range(a,b+1):
    for j in range(c,d+1):
        if is_prime(i+j):
            print('Takahashi')
            exit()
print('Aoki')

=======
Suggestion 3

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
        return True

a,b,c,d = map(int,input().split())

for i in range(a,b+1):
    for j in range(c,d+1):
        if is_prime(i+j):
            print("Aoki")
            exit()
print("Takahashi")

=======
Suggestion 4

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

=======
Suggestion 5

def isPrime(n):
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+2, 2):
            if n % i == 0:
                return False
        return True

A, B, C, D = map(int, input().split())
for i in range(B, D+1):
    if isPrime(i):
        print('Aoki')
        exit()
print('Takahashi')
exit()

=======
Suggestion 6

def isPrime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
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

A, B, C, D = map(int, input().split())

for i in range(A, B+1):
    for j in range(C, D+1):
        if is_prime(i+j):
            print("Takahashi")
            exit()
print("Aoki")

=======
Suggestion 8

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i ==0:
            return False
    return True

=======
Suggestion 9

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    i = 3
    while i <= n**0.5:
        if n % i == 0: return False
        i += 2
    return True

=======
Suggestion 10

def prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

a,b,c,d = map(int, input().split())
for i in range(a,b+1):
    for j in range(c,d+1):
        if prime(i+j):
            print("Aoki")
            exit()
print("Takahashi")
