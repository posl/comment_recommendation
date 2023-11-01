Synthesizing 10/10 solutions

=======
Suggestion 1

def getprime(n):
    prime = []
    for i in range(2, n+1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag

=======
Suggestion 2

def getPrimeList(num):
    primeList = []
    for i in range(2,num+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:

=======
Suggestion 3

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

=======
Suggestion 4

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

=======
Suggestion 5

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:

=======
Suggestion 6

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(

=======
Suggestion 7

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    for i in range(

=======
Suggestion 8

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0

=======
Suggestion 9

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):

=======
Suggestion 10

def func(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return 1, n
