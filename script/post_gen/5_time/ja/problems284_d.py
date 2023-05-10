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

t = int(input())
for i in range(t):
    n = int(input())
    a = prime_factorize(n)
    print(a[0], a[1])

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if not n % i:
            return False
        i += 1
    return True

=======
Suggestion 3

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        p = 0
        q = 0
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                p = j
                q = n // j
                break
        print(p, q)

=======
Suggestion 4

def prime_num(n):
    if n < 2:
        return []
    prime = [2]
    limit = int(n**0.5)
    data = [i+1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

=======
Suggestion 5

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


n = int(input())
for _ in range(n):
    num = int(input())
    table = prime_decomposition(num)
    p = table[0]
    q = table[1]
    print(p, q)

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True

=======
Suggestion 7

def get_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            factors.append(i)
        i += 1
    if n > 1:
        factors.append(n)
    return factors

T = int(input())
for i in range(T):
    N = int(input())
    factors = get_prime_factors(N)
    p = factors[0]
    q = factors[1]
    print("{} {}".format(p, q))

=======
Suggestion 8

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        for j in range(2,int(n**0.5)+1):
            if n%j == 0:
                print(j,int(n/j))
                break

=======
Suggestion 9

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

=======
Suggestion 10

def solve(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None
