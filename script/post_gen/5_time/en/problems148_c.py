Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

A, B = map(int, input().split())
print(A * B // gcd(A, B))

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a, b = map(int, input().split())
print(a * b // gcd(a, b))

=======
Suggestion 3

def lcm(a, b):
    from fractions import gcd
    return (a * b) // gcd(a, b)

a, b = map(int, input().split())
print(lcm(a, b))

=======
Suggestion 4

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A,B = map(int,input().split())
print(A*B//gcd(A,B))

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    print(a*b)

=======
Suggestion 6

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

=======
Suggestion 7

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    print(a*b)
    return
