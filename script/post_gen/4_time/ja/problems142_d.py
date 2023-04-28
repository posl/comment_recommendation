Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
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
Suggestion 2

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

a, b = map(int, input().split())
g = gcd(a, b)
ans = 1
for i in range(2, int(g**0.5)+1):
    if g % i == 0:
        ans += 1
        while g % i == 0:
            g //= i

=======
Suggestion 3

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 4

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
Suggestion 5

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

a,b = map(int,input().split())

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())
n = gcd(a, b)
cnt = 1

for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        cnt += 1
        while n % i == 0:
            n //= i

=======
Suggestion 7

def gcd(x,y):
    if x < y:
        x,y = y,x
    if x % y == 0:
        return y
    else:
        for i in range(y,0,-1):
            if x % i == 0 and y % i == 0:
                return i

a,b = map(int,input().split())
n = gcd(a,b)
ans = 1
