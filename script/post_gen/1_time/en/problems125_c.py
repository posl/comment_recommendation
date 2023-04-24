Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)

=======
Suggestion 6

def gcd(a,b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
