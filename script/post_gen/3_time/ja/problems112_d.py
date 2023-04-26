Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n, m = map(int, input().split())

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

N, M = map(int, input().split())
L = [int(i) for i in range(M//N, 0, -1) if M % i == 0]
for i in L:
    if M//i >= N:
        print(i)
        break

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
a = list(map(int, input().split()))

g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 5

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N, M = map(int, input().split())

for i in range(1, int(M ** 0.5) + 1):
    if M % i == 0:
        j = M // i
        if i * N <= M:
            ans = i
        if j * N <= M:
            ans = j

print(ans)

=======
Suggestion 6

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N, M = map(int, input().split())
A = list(map(int, input().split()))
g = 0
for i in range(N):
    g = gcd(g, A[i])
print(g)

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 8

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

n,m=map(int,input().split())
a=gcd(n,m)
print(m//a)

=======
Suggestion 9

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

N,M = map(int,input().split())
print(gcd(M,N))

=======
Suggestion 10

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A = A[::-1]
