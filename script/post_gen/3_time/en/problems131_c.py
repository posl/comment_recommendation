Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D = map(int, input().split())
    print(B - A + 1 - (B // C - (A - 1) // C) - (B // D - (A - 1) // D) + (B // (C * D // math.gcd(C, D)) - (A - 1) // (C * D // math.gcd(C, D))))

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

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 5

def gcd(a,b):
    if a<b:
        a,b = b,a
    while b>0:
        a,b = b,a%b
    return a
