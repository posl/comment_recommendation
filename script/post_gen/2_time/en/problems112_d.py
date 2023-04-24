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
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 4

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

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
    N, M = map(int, input().split())
    a = M // N
    if M % N == 0:
        print(a)
    else:
        print(a - 1)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    print(M // N)
