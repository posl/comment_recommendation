Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

a,b = map(int,input().split())
g = gcd(a,b)
l = a*b//g
print(l)

=======
Suggestion 2

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

a,b=map(int,input().split())
g=gcd(a,b)
print(a*b//g)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
c = gcd(a, b)
print(a * b // c)

=======
Suggestion 4

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

A,B=map(int,input().split())
g=gcd(A,B)
lcm=A*B//g
print(lcm)

=======
Suggestion 5

def lcm(x, y):
    return (x * y) // gcd(x, y)

=======
Suggestion 6

def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm

a, b = map(int, input().split())
print(lcm(a, b))

=======
Suggestion 7

def lcm(a,b):
    return a*b//gcd(a,b)

=======
Suggestion 8

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
g = gcd(a, b)
print(a * b // g)

=======
Suggestion 9

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 10

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
