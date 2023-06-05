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

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 3

def gcd(a,b):
    if a<b:
        a,b=b,a
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

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

k = int(input())
ans = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        for c in range(1,k+1):
            ans += gcd(a,gcd(b,c))
print(ans)

=======
Suggestion 5

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

k = int(input())
sum = 0
for a in range(1, k+1):
    for b in range(1, k+1):
        for c in range(1, k+1):
            sum += gcd(a, gcd(b, c))

print(sum)

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 8

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
