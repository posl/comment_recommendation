Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 3

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a, b = map(int, input().split())
g = gcd(a, b)
ans = 1
for i in range(2, int(g**0.5) + 1):
    if g % i == 0:
        ans += 1
        while g % i == 0:
            g //= i

=======
Suggestion 4

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
ans = 1
for i in range(2, int(g ** 0.5) + 1):
    if g % i == 0:
        ans += 1
        while g % i == 0:
            g //= i

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
A, B = map(int, input().split())
g = gcd(A, B)
ans = 1
for i in range(2, int(g ** 0.5) + 1):
    if g % i == 0:
        ans += 1
        while g % i == 0:
            g //= i

=======
Suggestion 7

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a,b = map(int, input().split())
g = gcd(a,b)
cnt = 1
for i in range(2, int(g**0.5)+1):
    if g%i == 0:
        cnt += 1
        if i != g//i:
            cnt += 1
print(cnt)

=======
Suggestion 9

def gcd(a,b):
    return a if b==0 else gcd(b,a%b)

A,B=map(int,input().split())
g=gcd(A,B)
c=1
for i in range(2,int(g**0.5)+1):
    if g%i==0:
        c+=1
        while g%i==0:
            g//=i
