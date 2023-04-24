Synthesizing 10/10 solutions

=======
Suggestion 1

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

=======
Suggestion 2

def prime_factorization(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

=======
Suggestion 3

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 5

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 6

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

=======
Suggestion 7

def isprime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

=======
Suggestion 8

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        for p in range(2, int(N**0.5)+1):
            if N%p == 0:
                q = N//p
                break
        print(p, q)

=======
Suggestion 9

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        for i in range(2, int(N**0.5)+1):
            if N%i==0:
                print(i, N//i)
                break

=======
Suggestion 10

def main():
    N = int(input())
    p = 0
    q = 0
    for i in range(2, N + 1):
        if N % i == 0:
            p = i
            break
    q = N // p
    print(p, q)
