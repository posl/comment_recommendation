Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 6

def gcd(x,y):
    if x < y:
        x,y = y,x
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

K = int(input())
ans = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            ans += gcd(a,gcd(b,c))
print(ans)

=======
Suggestion 7

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

=======
Suggestion 8

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
