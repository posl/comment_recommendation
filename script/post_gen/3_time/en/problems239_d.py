Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

=======
Suggestion 2

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())
for i in range(A, B + 1):
    for j in range(C, D + 1):
        if is_prime(i + j):
            print('Aoki')
            exit()
print('Takahashi')

=======
Suggestion 3

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

A,B,C,D = map(int, input().split())

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

a, b, c, d = map(int, input().split())
count = 0
for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i + j):
            count += 1

=======
Suggestion 5

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

=======
Suggestion 6

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    return not any(n % i == 0 for i in range(3, int(n**0.5)+1, 2))

A, B, C, D = map(int, input().split())

for i in range(A, B+1):
    for j in range(C, D+1):
        if is_prime(i+j):
            print('Aoki')
            exit()
print('Takahashi')

=======
Suggestion 7

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

=======
Suggestion 8

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

A, B, C, D = map(int, input().split())
for i in range(A, B+1):
    for j in range(C, D+1):
        if isPrime(i+j):
            print("Aoki")
            exit()
print("Takahashi")

=======
Suggestion 9

def isPrime(num):
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
