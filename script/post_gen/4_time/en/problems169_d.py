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

N = int(input())
factors = prime_factorize(N)
ans = 0
for i in range(len(factors)):
    if i == 0:
        ans += factors[i] - 1
    else:
        ans += factors[i]
print(ans)

import math
N = int(input())
ans = 0
for i in range(2, int(math.sqrt(N)) + 1):
    while N % i == 0:
        N = N // i
        ans += 1

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N**0.5)+1):
        while N % i == 0:
            N //= i
            ans += 1
    if N != 1:
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = 0
    z = 2
    while z*z <= N:
        while N % z == 0:
            N //= z
            ans += 1
        z += 1
    if N > 1:
        ans += 1
    print(ans)

=======
Suggestion 4

def get_primes(n):
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

=======
Suggestion 5

def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N**0.5)+1):
        while N%i == 0:
            ans += 1
            N //= i
    if N > 1:
        ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())

    # 素因数分解
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

    factors = prime_factorization(N)
    print(len(set(factors)))

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for p in range(2, 40):
        for e in range(1, 40):
            if N % (p**e) == 0:
                ans = e
    print(ans)

=======
Suggestion 8

def get_primes(max_num):
    # get primes under max_num
    primes = [2, 3]
    for i in range(5, max_num, 2):
        for j in range(3, int(i**0.5)+1, 2):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
