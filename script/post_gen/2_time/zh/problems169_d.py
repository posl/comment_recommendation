Synthesizing 10/10 solutions

=======
Suggestion 1

def get_prime_factors(n):
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

def prime_decomposition(n):
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
Suggestion 3

def main():
    N = int(input())
    # N = 997764507000
    # N = 24
    # N = 64
    # N = 1000000007
    # N = 1
    # N = 2
    # N = 3
    # N = 4
    # N = 5
    # N = 6
    # N = 7
    # N = 8
    # N = 9
    # N = 10
    # N = 11
    # N = 12
    # N = 13
    # N = 14
    # N = 15
    # N = 16
    # N = 17
    # N = 18
    # N = 19
    # N = 20
    # N = 21
    # N = 22
    # N = 23
    # N = 25
    # N = 26
    # N = 27
    # N = 28
    # N = 29
    # N = 30
    # N = 31
    # N = 32
    # N = 33
    # N = 34
    # N = 35
    # N = 36
    # N = 37
    # N = 38
    # N = 39
    # N = 40
    # N = 41
    # N = 42
    # N = 43
    # N = 44
    # N = 45
    # N = 46
    # N = 47
    # N = 48
    # N = 49
    # N = 50
    # N = 51
    # N = 52
    # N = 53
    # N = 54
    # N = 55
    # N = 56
    # N = 57
    # N = 58
    # N = 59
    # N = 60
    # N = 61
    # N = 62
    # N = 63
    # N = 65
    # N = 66
    # N = 67
    # N

=======
Suggestion 4

def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            while N % i == 0:
                N //= i
            ans += 1
    if N != 1:
        ans += 1
    print(ans)

=======
Suggestion 5

def primeFactorization(n):
    primeFactor = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            t = 0
            while n % i == 0:
                n /= i
                t += 1
            primeFactor.append(i ** t)
        i += 1

    if n != 1:
        primeFactor.append(n)

    return primeFactor

N = int(input())
p = primeFactorization(N)
print(len(p))

=======
Suggestion 6

def prime_factorization(n):
    prime_factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n /= i
        i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors

=======
Suggestion 7

def get_prime_factors(n):
    factors = []
    divisor = 2
    while(divisor <= n):
        if n % divisor == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return factors

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            m = n
            while m % i == 0:
                m //= i
            if m % i == 1:
                m = n
                while m % i == 0:
                    m //= i
                ans += 1
    m = n - 1
    for i in range(2, int(m ** 0.5) + 1):
        if m % i == 0:
            ans += 1
            while m % i == 0:
                m //= i
    if m != 1:
        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    # 1. N是素数，直接输出0
    if is_prime(N):
        print(0)
        return
    # 2. N不是素数，分解质因数
    else:
        factor = prime_factorization(N)
        # print(factor)
        # 3. 分解质因数中，出现1次的质因数个数
        count = 0
        for key, value in factor.items():
            if value == 1:
                count += 1
        print(count)

=======
Suggestion 10

def gcd(a,b):
    if a<b:
        a,b = b,a
    while b!=0:
        a,b = b,a%b
    return a
