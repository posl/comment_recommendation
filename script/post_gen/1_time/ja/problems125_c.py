Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
A = list(map(int, input().split()))

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
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_gcd = 0
    for i in range(N):
        if i == 0:
            max_gcd = gcd(A[i+1], A[i])
        elif i == N-1:
            max_gcd = max(max_gcd, gcd(A[i-1], A[i]))
        else:
            max_gcd = max(max_gcd, gcd(A[i-1], A[i+1]))
    print(max_gcd)
