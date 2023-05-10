Synthesizing 10/10 solutions

=======
Suggestion 1

def lcm(x, y):
    return (x * y) // gcd(x, y)

=======
Suggestion 2

def calc_gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 3

def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)

a,b=map(int,input().split())
g=gcd(a,b)
l=a*b//g
print(l)

=======
Suggestion 4

def solve():
    a, b = map(int, input().split())
    print((a * b) // math.gcd(a, b))

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

a, b = map(int, input().split())
g = gcd(a, b)
print(a * b // g)

=======
Suggestion 7

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

a,b = map(int,input().split())
c = gcd(a,b)
print(a*b//c)

=======
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a,b = map(int,input().split())

c = gcd(a,b)
d = a*b//c

print(d)

=======
Suggestion 9

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

=======
Suggestion 10

def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

a, b = map(int, input().split())
print(lcm(a, b))
