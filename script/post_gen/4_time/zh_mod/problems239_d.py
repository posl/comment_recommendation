Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i*i <= x:

=======
Suggestion 2

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 ==0:
        return False
    for i i

=======
Suggestion 3

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i i

=======
Suggestion 5

def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False

=======
Suggestion 6

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1): #只需要判定到根号n
        if n % i == 0:
            re

=======
Suggestion 7

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            retu

=======
Suggestion 8

def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                re

=======
Suggestion 9

def is_prime(n):
    if n==1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True

=======
Suggestion 10

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                re
