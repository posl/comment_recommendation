Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if a < b:
        a,b = b,a
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 2

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n,m = map(int,input().split())

=======
Suggestion 3

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

n, m = map(int, input().split())

=======
Suggestion 4

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 5

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n,m = map(int, input().split())
ans = 1
for i in range(1, int(m**0.5)+1):
    if m % i == 0:
        if m//i >= n:
            ans = max(ans, i)
        if i >= n:
            ans = max(ans, m//i)

print(ans)

=======
Suggestion 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
#n, m = 100000, 1000000000
g = gcd(m, n)
m = m // g
n = n // g
ans = 1
i = 2
while i * i <= m:
    if m % i == 0:
        ans = max(ans, i)
        while m % i == 0:
            m //= i
    i += 1

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 9

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)

N, M = map(int, input().split())
max_gcd = 0
for i in range(1, int(M/N)+1):
    if M % i == 0:
        max_gcd = max(max_gcd, gcd(i, M//i))

print(max_gcd)
