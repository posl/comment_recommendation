Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

=======
Suggestion 2

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

k = int(input())
sum = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        for l in range(1,k+1):
            sum += gcd(gcd(i,j),l)
print(sum)

=======
Suggestion 3

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

K=int(input())
sum=0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            sum+=gcd(gcd(a,b),c)
print(sum)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a%b
    return b

=======
Suggestion 5

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

K = int(input())
sum = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            sum += gcd(gcd(a, b), c)
print(sum)

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 7

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 8

def gcd(a,b,c):
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
    if a>b:
        a,b=b,a
    if a==0:
        return b
    else:
        return gcd(a,b%a,c)

=======
Suggestion 9

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

K=int(input())
ans=0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            ans+=gcd(gcd(a,b),c)
print(ans)
