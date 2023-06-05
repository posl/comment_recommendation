Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

=======
Suggestion 3

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5)+1):
            if n % i == 0:
                return False
        return True

a, b, c, d = map(int, input().split())

=======
Suggestion 4

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

a,b,c,d = map(int,input().split())

=======
Suggestion 5

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    if is_prime(i):
        for j in range(c, d+1):
            if is_prime(j):
                if i + j == 2 or (i + j) % 2 == 1:
                    print("High")
                    exit()
print("Low")

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    i = 2
    while i <= n**0.5:
        if n % i == 0:
            return False
        i += 1
    return True

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    if is_prime(i):
        for j in range(c, d+1):
            if is_prime(j):
                if i+j == 13:
                    print("高桥")
                    exit()
print("青木")

=======
Suggestion 8

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
Suggestion 9

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True

a,b,c,d = map(int,input().split())
for i in range(a,b+1):
    for j in range(c,d+1):
        if is_prime(i+j):
            print('高桥')
            exit()
print('青木')

=======
Suggestion 10

def is_prime(x):
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
