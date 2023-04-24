Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

K = int(input())
ans = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            ans += gcd(gcd(a,b),c)
print(ans)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

k = int(input())
ans = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            ans += gcd(gcd(a, b), c)
print(ans)

=======
Suggestion 4

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

k = int(input())
ans = 0
for i in range(1,k+1):
    for j in range(1,k+1):
        for l in range(1,k+1):
            ans += gcd(i,gcd(j,l))
print(ans)

=======
Suggestion 5

def gcd(a, b, c):
    ret = 1
    for i in range(2, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            ret = i
    return ret

K = int(input())
ans = 0
for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            ans += gcd(a, b, c)
print(ans)

=======
Suggestion 6

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

K = int(input())
ans = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            ans += gcd(gcd(a,b),c)
print(ans)

=======
Suggestion 7

def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a
