Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a, b = map(int, input().split())

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
g = gcd(a, b)
ans = 1
for i in range(2, int(g ** 0.5) + 1):
    if g % i == 0:
        ans += 1
        while g % i == 0:
            g //= i

=======
Suggestion 4

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

a, b = map(int, input().split())
g = gcd(a, b)
ans = 1
for i in range(2, int(g**0.5)+1):
    if g%i == 0:
        ans += 1
        while g%i == 0:
            g //= i

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())
g = gcd(a, b)
cnt = 1
for i in range(2, int(g**0.5)+1):
    if g % i == 0:
        cnt += 1
        while g % i == 0:
            g //= i

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

A, B = map(int, input().split())
g = gcd(A, B)
ans = 1
for i in range(2, int(g**0.5)+1):
    if g%i == 0:
        ans += 1
        while g%i == 0:
            g //= i

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())
gcd_ab = gcd(a, b)
ans = 1
for i in range(2, int(gcd_ab**0.5)+1):
    if gcd_ab % i == 0:
        ans += 1
        while gcd_ab % i == 0:
            gcd_ab //= i

=======
Suggestion 10

def gcd(x,y):
    if x<y:
        x,y=y,x
    while y>0:
        x,y=y,x%y
    return x
