Synthesizing 10/10 solutions

=======
Suggestion 1

def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i==0:
            return False
    return True

a, b, c, d = map(int, input().split())

for i in range(100):
    if prime(a + b - i):
        print('高桥')
        break
    elif prime(c + d - i):
        print('青木')
        break

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    if is_prime(i+c) == True:
        print("高桥")
        exit()
print("青木")

=======
Suggestion 3

def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

A,B,C,D = map(int,input().split())
for i in range(B+1,D+2):
    if is_prime(i):
        if i == A+C or i == A+D or i == B+C or i == B+D:
            print("High")
            exit()
print("Low")

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i+j):
            print("高桥")
            exit(0)
print("青木")

=======
Suggestion 5

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i ==0:
            return False
    return True

a, b, c, d = map(int, input().split())
for i in range(a, b+1):
    if isPrime(i):
        for j in range(c, d+1):
            if isPrime(j):
                if i+j == 9:
                    print("高桥")
                    exit()
                else:
                    print("青木")
                    exit()

=======
Suggestion 6

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): #平方根まで
        if n%i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): # n**0.5+1
        if n % i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())

=======
Suggestion 8

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

for n in range(1, 100):
    if a <= n <= b and c <= n <= d:
        print('High') if is_prime(n) else print('Low')
        exit()

=======
Suggestion 9

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i == 0:
                return False
        return True

=======
Suggestion 10

def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True
