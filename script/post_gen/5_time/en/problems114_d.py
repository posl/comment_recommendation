Synthesizing 10/10 solutions (Duplicates hidden)

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
d = {}
for i in range(1, n+1):
    for j in prime_factorize(i):
        if j in d:
            d[j] += 1
        else:
            d[j] = 1

ans = 0
for i in d.values():
    if i >= 74:
        ans += 1
for i in d.values():
    for j in d.values():
        if i != j and i >= 24 and j >= 2:
            ans += 1
for i in d.values():
    for j in d.values():
        if i != j and i >= 14 and j >= 4:
            ans += 1
for i in d.values():
    for j in d.values():
        if i != j and i >= 4 and j >= 4:
            for k in d.values():
                if k != i and k != j and k >= 2:
                    ans += 1
print(ans)

=======
Suggestion 3

def factorize(n):
    fct = []
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

=======
Suggestion 4

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
Suggestion 5

def factorize(n):
    fct = []
    b,e = 2,0
    while b*b <= n:
        while n % b == 0:
            n = n//b
            e = e+1
        if e > 0:
            fct.append((b,e))
        b,e = b+1,0
    if n > 1:
        fct.append((n,1))
    return fct

N = int(input())
factors = factorize(N)
print(factors)
ans = 0
for f in factors:
    if f[1] >= 74:
        ans += 1
print(ans)

=======
Suggestion 6

def factorize(n):
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n //= b
            e += 1
        if e > 0:
            yield b, e
            b, e = b + 1, 0
    if n > 1:
        yield n, 1

=======
Suggestion 7

def get_prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

=======
Suggestion 8

def is_prime(n):
    if n == 1:
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
