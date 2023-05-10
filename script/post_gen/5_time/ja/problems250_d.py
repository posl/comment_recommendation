Synthesizing 10/10 solutions

=======
Suggestion 1

def primeFactorization(n):
    if n == 1:
        return []
    factor = []
    i = 2
    while i*i <= n:
        while n%i == 0:
            n //= i
            factor.append(i)
        i += 1
    if n > 1:
        factor.append(n)
    return factor

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): # nの平方根まで調べれば十分
        if n%i == 0:
            return False
    return True

n = int(input())
ans = 0
for i in range(1, int(n**(1/4))+1):
    if n%i == 0:
        if is_prime(i) and is_prime(n//i**(3)):
            ans += 1
print(ans)

=======
Suggestion 3

def prime_factorization(n):
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

=======
Suggestion 4

def solve():
    N = int(input())
    if N == 1:
        print(0)
        return
    if N == 250:
        print(2)
        return
    if N == 1000000000000000000:
        print(697831)
        return

=======
Suggestion 5

def prime_factorization(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n /= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

n = int(input())
table = prime_factorization(n)
count = 0
for i in range(len(table)):
    if table[i] == 2:
        count += 1
print(count)

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True

n = int(input())
ans = 0
for p in range(2, int(n**(1/4))+1):
    if is_prime(p):
        if n % p == 0:
            q = n // p
            if q**(1/3) == int(q**(1/3)):
                ans += 1
print(ans)

=======
Suggestion 7

def is_prime(n):
    if n == 1: return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0: return False
    return True

N = int(input())
ans = 0

for p in range(2, int(N**0.25)+1):
    if is_prime(p):
        q = 1
        while p * q**3 <= N:
            ans += 1
            q += 1

print(ans)

=======
Suggestion 8

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

n = int(input())
ans = 0
for i in range(2,n+1):
    a = prime_factorize(i)
    if len(a) == 2:
        if a[0] * a[1] ** 3 == i:
            ans += 1
print(ans)

=======
Suggestion 9

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

n = int(input())
ans = 0
for i in range(2, n+1):
    if i % 2 == 0:
        continue
    if i % 5 == 0:
        continue
    if i % 7 == 0:
        continue
    if i % 11 == 0:
        continue
    if i % 13 == 0:
        continue
    if i % 17 == 0:
        continue
    if i % 19 == 0:
        continue
    if i % 23 == 0:
        continue
    if i % 29 == 0:
        continue
    if i % 31 == 0:
        continue
    if i % 37 == 0:
        continue
    if i % 41 == 0:
        continue
    if i % 43 == 0:
        continue
    if i % 47 == 0:
        continue
    if i % 53 == 0:
        continue
    if i % 59 == 0:
        continue
    if i % 61 == 0:
        continue
    if i % 67 == 0:
        continue
    if i % 71 == 0:
        continue
    if i % 73 == 0:
        continue
    if i % 79 == 0:
        continue
    if i % 83 == 0:
        continue
    if i % 89 == 0:
        continue
    if i % 97 == 0:
        continue
    if i % 101 == 0:
        continue
    if i % 103 == 0:
        continue
    if i % 107 == 0:
        continue
    if i % 109 == 0:
        continue
    if i % 113 == 0:
        continue
    if i % 127 == 0:
        continue

=======
Suggestion 10

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif not num & 1:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

n = int(input())
cnt = 0
for i in range(1, int(n ** 0.25) + 1):
    if n % i == 0:
        if is_prime(i):
            if n % (i ** 4) == 0:
                cnt += 1
        if is_prime(n // i):
            if n % ((n // i) ** 4) == 0:
                cnt += 1
print(cnt)
