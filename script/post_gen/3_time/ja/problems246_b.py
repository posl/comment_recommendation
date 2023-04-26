Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    s = (a ** 2 + b ** 2) ** 0.5
    print(a / s, b / s)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print(A / (A + B), B / (A + B))

=======
Suggestion 3

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

A, B = map(int, input().split())
g = gcd(A, B)
print(A/g, B/g)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    C = (A**2 + B**2)**(1/2)
    print(A/C, B/C)

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    c = (a**2+b**2)**0.5
    print(a/c,b/c)

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    # A, B = 246, 402
    # A, B = 1, 0
    # A, B = 3, 4
    import math
    d = math.sqrt(A**2 + B**2)
    print(A/d, B/d)
