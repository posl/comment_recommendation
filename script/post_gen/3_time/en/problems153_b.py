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
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    print("Yes" if H <= sum(A) else "No")

=======
Suggestion 4

def main():
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H <= sum(A):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 8

def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 9

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

H, N = map(int, input().split())
A = list(map(int, input().split()))
g = A[0]
for i in range(1, N):
    g = gcd(g, A[i])
