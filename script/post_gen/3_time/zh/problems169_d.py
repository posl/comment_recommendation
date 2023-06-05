Synthesizing 10/10 solutions

=======
Suggestion 1

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 1:
        factors.append(n)
    return factors

=======
Suggestion 2

def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2
    return True

=======
Suggestion 3

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
Suggestion 4

def main():
    n = int(input())
    z = 2
    cnt = 0
    while n > 1:
        if n % z == 0:
            n = n // z
            cnt += 1
        else:
            z += 1
    print(cnt)

=======
Suggestion 5

def main():
    N = int(input())
    result = 0
    i = 2
    while i*i <= N:
        if N%i == 0:
            result += 1
            while N%i == 0:
                N //= i
        i += 1
    if N != 1:
        result += 1
    print(result)
    
main()

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

=======
Suggestion 7

def prime_factorization(n):
    if n == 1:
        return []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + prime_factorization(n // i)
    return [n]

=======
Suggestion 8

def prime_factorization(n):
    if n == 1:
        return [1]
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

n = int(input())
factors = prime_factorization(n)
fact_set = set(factors)
ans = 0
for fact in fact_set:
    tmp = 0
    while n % fact == 0:
        n //= fact
        tmp += 1
    if tmp == 0:
        continue
    i = 1
    while i * i <= tmp:
        if tmp % i == 0:
            if i in fact_set:
                ans += 1
            if tmp // i in fact_set:
                ans += 1
        i += 1
    if tmp * tmp == tmp and tmp in fact_set:
        ans -= 1

=======
Suggestion 9

def prime_factorization(n):
    i = 2
    table = []
    while i**2 <= n:
        while n%i == 0:
            n = n//i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

=======
Suggestion 10

def primeFactorization(n):
    i = 2
    primeList = []
    while i * i <= n:
        if n % i == 0:
            primeList.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        primeList.append(n)
    return primeList

n = int(input())
primeList = primeFactorization(n)
ans = 0
for i in range(1, len(primeList)):
    if primeList[i] != primeList[i - 1]:
        ans += 1
print(ans)
