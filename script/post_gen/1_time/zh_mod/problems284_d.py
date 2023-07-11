Synthesizing 10/10 solutions

=======
Suggestion 1

def judge(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

=======
Suggestion 2

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or

=======
Suggestion 3

def isPrime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2, int(n*

=======
Suggestion 4

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for x in range(2, n)

=======
Suggestion 5

def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:

=======
Suggestion 6

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(pow(n, 0.5))+1):
        if n % i

=======
Suggestion 7

def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):

=======
Suggestion 8

def get_prime(n):
    prime_list = []
    for i in range(2, n+1):
        for j in range(2, i):
            if

=======
Suggestion 9

def getPrime(num):
    prime = []
    for i in range(2,num+1):
        if i == 2:
            prime.append(i)

=======
Suggestion 10

def isPrime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return
