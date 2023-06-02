Synthesizing 10/10 solutions

=======
Suggestion 1

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

=======
Suggestion 2

def isPrime(n):
    if n == 2:
        return True
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

=======
Suggestion 3

def get_prime_list(n):
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

=======
Suggestion 4

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i = i + 6
    return True

t = int(input())
for i in range(t):
    n = int(input())
    p = 0
    q = 0
    for j in range(2, n):
        if isPrime(j) and n % j == 0:
            p = j
            q = int(n / p)
            break
    print(p, q)

=======
Suggestion 5

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True

=======
Suggestion 6

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 6 != 1 and n % 6 != 5:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

=======
Suggestion 7

def get_prime(n):
    prime = []
    for i in range(2, n+1):
        flag = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                flag = False
        if flag:
            prime.append(i)
    return prime

=======
Suggestion 8

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(pow(n, 0.5)) + 1):
            if n % i == 0:
                return False
        return True

=======
Suggestion 9

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

=======
Suggestion 10

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
