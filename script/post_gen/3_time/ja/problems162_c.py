Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    ans = 0
    for a in range(1, K+1):
        for b in range(1, K+1):
            for c in range(1, K+1):
                ans += gcd(gcd(a, b), c)
    print(ans)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 5

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

K = int(input())
ans = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            ans += gcd(gcd(a,b),c)
print(ans)

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

K = int(input())

ans = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            ans += gcd(a, gcd(b, c))
print(ans)

=======
Suggestion 7

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

K = int(input())
ans = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            ans += gcd(i,gcd(j,k))
print(ans)

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 9

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

K = int(input())
S = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            S += gcd(gcd(a,b),c)
print(S)
