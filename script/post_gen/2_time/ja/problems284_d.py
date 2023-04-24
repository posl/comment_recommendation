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

T = int(input())
for i in range(T):
    N = int(input())
    p = prime_factorize(N)
    p = list(set(p))
    q = N // (p[0] ** 2)
    print(p[0],q)

=======
Suggestion 2

def is_prime(n):
    if n==2:
        return True
    if n<2 or n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

=======
Suggestion 3

def is_prime(num):
    if num == 1:
        return False
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
Suggestion 4

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        p = 0
        q = 0
        for i in range(2, int(N**0.5)+1):
            if N % i == 0:
                p = i
                q = N // i
                break
        print(p, q)

=======
Suggestion 5

def getPrimeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

=======
Suggestion 6

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        for j in range(2, int(N**0.5)+1):
            if N % j == 0:
                p = j
                q = N // p // p
                print(p, q)
                break

=======
Suggestion 7

def is_prime(n):
    """素数判定"""
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

=======
Suggestion 8

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        for j in range(2, int(N**0.5)+1):
            if N%(j**2)==0:
                p = j
                q = N//(j**2)
                break
        print(p, q)

=======
Suggestion 9

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        for j in range(2, int(n**0.5)+1):
            if n % j == 0:
                k = n // j
                if k % j == 0:
                    print(j, k // j)
                    break

=======
Suggestion 10

def prime_factorization(n):
    """素因数分解する関数
    引数
    n:整数
    返り値
    list:素因数分解の結果
    """
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table
