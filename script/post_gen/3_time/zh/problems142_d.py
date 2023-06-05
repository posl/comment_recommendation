Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

a, b = map(int, input().split())
g = gcd(a, b)
cnt = 1
for i in range(2, int(g**0.5)+1):
    if g % i == 0:
        cnt += 1
        while g % i == 0:
            g //= i

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a,b=map(int,input().split())
g=gcd(a,b)
ans=1
for i in range(2,int(g**0.5)+1):
    if g%i==0:
        ans+=1
        while g%i==0:
            g//=i

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
    return gcd(b, a % b)

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
a, b = map(int, input().split())
g = gcd(a, b)

=======
Suggestion 7

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

a, b = map(int, input().split())

=======
Suggestion 8

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())
g = gcd(a, b)
cnt = 0
for i in range(1, g+1):
    if gcd(a, b) == 1:
        cnt += 1
print(cnt)
