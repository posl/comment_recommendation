Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

A, B = map(int, input().split())

print(int(A/gcd(A, B))*B)

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

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
print(a * b // gcd(a, b))

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

A, B = map(int, input().split())
print(A * B // gcd(A, B))

I have a problem with this code. I have a problem with this code.

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B = map(int, input().split())
print(A * B // gcd(A, B))

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

A, B = map(int, input().split())
print((A * B) // gcd(A, B))

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 8

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    print(A * B // math.gcd(A, B))

=======
Suggestion 10

def main():
    a,b = map(int,input().split())
    print(a*b//math.gcd(a,b))
