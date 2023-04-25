Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(A, B, g):
    return (A / (g ** 0.5)) + B

A, B = map(int, input().split())
g = 1
while True:
    if f(A, B, g) >= f(A, B, g + 1):
        print(f(A, B, g))
        break
    else:
        g += 1

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print((A + B) ** 0.5 - B)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print((A/B)**(1/2))

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print((A + B) / 2)

=======
Suggestion 6

def solve(A, B):
    import math
    g = 1
    t = 0
    while True:
        t += A / (g ** 0.5)
        if g + B > A:
            t += A / ((g + B) ** 0.5)
            break
        else:
            g += B
    return t

=======
Suggestion 7

def solve():
    a, b = map(int, input().split())
    if b >= a:
        return 1 + (a / 2)
    else:
        return 1 + b + (a / (2 * b))

=======
Suggestion 8

def main():
    A,B = map(int,input().split())
    g = 1
    time = 0
    while(True):
        if A >= (B * time) / (g ** (1/2)):
            time += 1
            g += 1
        else:
            break
    time -= 1
    print((time + (A / (g ** (1/2)))))

=======
Suggestion 9

def solve(a,b):
    return ((a**3)/(b**2))**(1/2)
