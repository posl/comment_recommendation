Synthesizing 10/10 solutions

=======
Suggestion 1

def get_prime_factors(n):
    factors = []
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            factors.append(i)
            while n%i == 0:
                n = n//i
    if n > 1:
        factors.append(n)
    return factors

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(2, N):
        if N % i == 0:
            ans += 1
            N = N // i
            if N == 1:
                break
    print(ans)

=======
Suggestion 3

def prime_factorize(n):
    # 素因数分解
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
a = prime_factorize(n)
b = list(set(a))
c = sorted(b)
ans = 0
for i in c:
    ans += a.count(i)
print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    while n > 1:
        ans += 1
        #print("n=", n)
        max = 0
        maxp = 0
        for p in range(2, int(n**0.5)+1):
            if n % p == 0:
                #print("p=", p)
                e = 0
                tmp = n
                while tmp % p == 0:
                    tmp = tmp // p
                    e += 1
                if e > max:
                    max = e
                    maxp = p
        if max == 0:
            break
        #print("maxp=", maxp)
        n = n // maxp
    print(ans)

=======
Suggestion 5

def check_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

=======
Suggestion 6

def find_max_times(n):
    result = 0
    for i in range(2, int(pow(n, 0.5))+1):
        if n % i == 0:
            while n % i == 0:
                n /= i
            result += 1
    if n != 1:
        result += 1
    return result

=======
Suggestion 7

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

=======
Suggestion 8

def factorize(n):
    res = []
    if n == 1:
        return res
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            while n % i == 0:
                n //= i
    if n != 1:
        res.append(n)
    return res
n = int(input())
factors = factorize(n)
ans = 0
for p in factors:
    e = 0
    x = n
    while x % p == 0:
        x //= p
        e += 1
    ans = max(ans, e)
print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    ans = 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            m = n
            while m % i == 0:
                m //= i
            if m % i == 1:
                m = n
                while m % i == 0:
                    m //= i
                ans += 1
    m = n-1
    for i in range(2,int(m**0.5)+1):
        if m % i == 0:
            while m % i == 0:
                m //= i
            if m % i == 1:
                ans += 1
    print(ans)

=======
Suggestion 10

def factorization(n):
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
