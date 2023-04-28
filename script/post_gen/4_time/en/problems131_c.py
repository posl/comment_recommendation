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

def main():
    A, B, C, D = map(int, input().split())
    print(B - A + 1 - (B // C - (A - 1) // C) - (B // D - (A - 1) // D) + (B // lcm(C, D) - (A - 1) // lcm(C, D)))

=======
Suggestion 3

def main():
    A, B, C, D = map(int, input().split())
    print(B - A + 1 - (B // C - (A - 1) // C) - (B // D - (A - 1) // D) + (B // C // D - (A - 1) // C // D))

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 6

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
