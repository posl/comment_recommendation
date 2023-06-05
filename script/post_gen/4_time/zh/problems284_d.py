Synthesizing 10/10 solutions

=======
Suggestion 1

def isPrime(n):
    if n <= 1:
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
Suggestion 2

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n%i == 0:
                return False
        return True

=======
Suggestion 3

def getPrimeList(n):
    primeList = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primeList.append(i)
    return primeList

=======
Suggestion 4

def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

=======
Suggestion 5

def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

=======
Suggestion 6

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

T = int(input())
for i in range(T):
    N = int(input())
    for p in range(2, int(N**(1/3))+1):
        if is_prime(p):
            if N % (p**2) == 0:
                print(p, N//(p**2))
                break

=======
Suggestion 7

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(pow(n, 0.5)) + 1, 2):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    for i in range(2, int(pow(n, 1 / 3)) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            print(i, n // i)
            break

=======
Suggestion 8

def prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

for i in range(int(input())):
    n = int(input())
    a = []
    for j in range(2, int(n**0.5)+1):
        if n % j == 0 and prime(j):
            a.append(j)
            a.append(n//j)
            break
    print(a[1], a[0])

=======
Suggestion 9

def prime(n):
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    p = int(n**0.5)
    while True:
        if prime(p) and n%p == 0:
            q = n//p//p
            if prime(q):
                print(p,q)
                break
        p += 1

=======
Suggestion 10

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
