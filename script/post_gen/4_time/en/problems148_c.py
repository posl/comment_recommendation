Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())
print(a*b//gcd(a, b))

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def lcm(x, y):
    from fractions import gcd
    return (x * y) // gcd(x, y)

=======
Suggestion 6

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

a,b=map(int,input().split())
g=gcd(a,b)
print(a*b//g)

=======
Suggestion 7

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

a,b = map(int,input().split())
print(a*b//gcd(a,b))

=======
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

A,B = map(int,input().split())
GCD = gcd(A,B)
LCM = int(A*B/GCD)
print(LCM)

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    print(A*B)
