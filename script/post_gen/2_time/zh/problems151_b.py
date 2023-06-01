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

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        while A[i] % 2 == 0:
            A[i] //= 2
    LCM = 1
    for i in range(N):
        LCM = LCM * A[i] // gcd(LCM, A[i])
    LCM *= 2
    ans = M // LCM
    return ans

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 6

def gcd(x,y):
    if x < y:
        x,y = y,x
    if y == 0:
        return x
    else:
        return gcd(y,x % y)

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

=======
Suggestion 8

def gcd(a,b):
    if a<b:
        a,b = b,a
    while b!=0:
        a,b = b,a%b
    return a
