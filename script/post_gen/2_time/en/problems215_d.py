Synthesizing 9/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

N, M = map(int, input().split())
A = list(map(int, input().split()))

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def generate_primes(n):
    primes = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n+1) if primes[p]]

=======
Suggestion 6

def main():
    #input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #gcd
    import fractions
    def gcd(*numbers):
        return fractions.gcd(*numbers)
    #solve
    def solve():
        import math
        g = gcd(*A)
        if g != 1:
            return 0
        ans = 0
        for i in range(1, M+1):
            if gcd(*A, i) == 1:
                ans += 1
        return ans
    #output
    print(solve())
