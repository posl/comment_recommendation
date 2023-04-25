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

N = int(input())
prime_list = prime_factorize(N)
prime_list = list(set(prime_list))
ans = 0
for i in prime_list:
    tmp = N
    while tmp % i == 0:
        tmp //= i
    if tmp % i == 1:
        ans += 1
print(ans)

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

N = int(input())
ans = 0
for i in prime_factorize(N):
    if i != 1:
        ans += 1
print(ans)

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

N = int(input())
a = prime_factorize(N)
#print(a)
a.sort()
#print(a)
ans = 0

=======
Suggestion 4

def prime_factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

n = int(input())

=======
Suggestion 5

def prime_factors(n):
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

n = int(input())
factors = prime_factors(n)
print(len(set(factors)))

=======
Suggestion 6

def get_prime_factors(n):
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

n = int(input())
factors = get_prime_factors(n)
factor_count = {}
for i in factors:
    if i not in factor_count:
        factor_count[i] = 0
    factor_count[i] += 1
max_count = 0
for i in factor_count:
    count = 0
    while factor_count[i] > 0:
        factor_count[i] -= i
        count += 1
    if count > max_count:
        max_count = count
print(max_count)

=======
Suggestion 7

def prime_factorize(n):
    if n == 1:
        return []
    factor = []
    while n % 2 == 0:
        factor.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            factor.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        factor.append(n)
    return factor

n = int(input())
factor = prime_factorize(n)
factor.sort()
length = len(factor)

=======
Suggestion 8

def main():
    N = int(input())
    i = 2
    ans = 0
    while i*i <= N:
        while N%i == 0:
            N //= i
            ans += 1
        i += 1
    if N > 1:
        ans += 1
    print(ans)
main()

=======
Suggestion 9

def prime_factorize(n):
    """nの素因数分解を返す"""
    divisors = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            divisors.append(i)
            n //= i
    if n > 1:
        divisors.append(n)
    return divisors

N = int(input())
divisors = prime_factorize(N)
divisors.sort()

=======
Suggestion 10

def prime_factorize(n):
    # 素因数分解
    # 2以上の整数n => [[素因数, 指数], ...]のリスト
    res = []
    for i in range(2, int(n**0.5)+1):
        if n%i != 0:
            continue
        ex = 0
        while n%i == 0:
            ex += 1
            n //= i
        res.append([i, ex])
    if n != 1:
        res.append([n, 1])
    return res

N = int(input())
ans = 0
for p, e in prime_factorize(N):
    tmp = 0
    while e >= tmp:
        tmp += 1
        e -= tmp
        ans += 1
print(ans)
