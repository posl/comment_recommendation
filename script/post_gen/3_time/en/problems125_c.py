Synthesizing 10/10 solutions (Duplicates hidden)

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
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
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

def gcd(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 2:
        print(max(A))
    else:
        A.sort()
        print(max(A[0], A[-2]))

=======
Suggestion 7

def gcd(a, b): return a if b == 0 else gcd(b, a % b)
