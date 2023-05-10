Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))

l = [0]*(n+1)
r = [0]*(n+1)

for i in range(n):
    l[i+1] = gcd(l[i],a[i])
    r[n-i-1] = gcd(r[n-i],a[n-i-1])

ans = 1
for i in range(n):
    ans = max(ans,gcd(l[i],r[i+1]))

print(ans)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

l = [0] * (n + 1)
r = [0] * (n + 1)
for i in range(n):
    l[i + 1] = gcd(l[i], a[i])
for i in range(n - 1, -1, -1):
    r[i] = gcd(r[i + 1], a[i])

ans = 0
for i in range(n):
    ans = max(ans, gcd(l[i], r[i + 1]))

print(ans)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())

a = list(map(int, input().split()))

left = [0] * n
right = [0] * n

left[0] = a[0]
right[-1] = a[-1]

for i in range(1, n):
    left[i] = gcd(left[i - 1], a[i])

for i in range(n - 2, -1, -1):
    right[i] = gcd(right[i + 1], a[i])

ans = 0

for i in range(n):
    if i == 0:
        ans = max(ans, right[i + 1])
    elif i == n - 1:
        ans = max(ans, left[i - 1])
    else:
        ans = max(ans, gcd(left[i - 1], right[i + 1]))

print(ans)

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
l = [0] * n
r = [0] * n
for i in range(n):
    if i == 0:
        l[i] = a[i]
        r[n - i - 1] = a[n - i - 1]
    else:
        l[i] = gcd(l[i - 1], a[i])
        r[n - i - 1] = gcd(r[n - i], a[n - i - 1])
ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, r[i + 1])
    elif i == n - 1:
        ans = max(ans, l[i - 1])
    else:
        ans = max(ans, gcd(l[i - 1], r[i + 1]))
print(ans)

=======
Suggestion 6

def gcd(a, b):
    # a >= b とする
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))
# a = [int(i) for i in input().split()]
a.sort()

g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])

print(g)

=======
Suggestion 8

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

l = [0] * n
r = [0] * n

l[0] = a[0]
r[n - 1] = a[n - 1]

for i in range(1, n):
    l[i] = gcd(l[i - 1], a[i])

for i in range(n - 2, -1, -1):
    r[i] = gcd(r[i + 1], a[i])

ans = max(l[n - 2], r[1])

for i in range(1, n - 1):
    ans = max(ans, gcd(l[i - 1], r[i + 1]))

print(ans)

=======
Suggestion 9

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

L = [0] * N
R = [0] * N

L[0] = A[0]
for i in range(1, N):
    L[i] = gcd(L[i - 1], A[i])

R[N - 1] = A[N - 1]
for i in range(N - 2, -1, -1):
    R[i] = gcd(R[i + 1], A[i])

ans = 1
for i in range(N):
    if i == 0:
        ans = max(ans, R[i + 1])
    elif i == N - 1:
        ans = max(ans, L[i - 1])
    else:
        ans = max(ans, gcd(L[i - 1], R[i + 1]))

print(ans)

=======
Suggestion 10

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))

l = [0 for _ in range(n)]
r = [0 for _ in range(n)]

l[0] = a[0]
r[n-1] = a[n-1]

for i in range(1, n):
    l[i] = gcd(l[i-1], a[i])

for i in range(n-2, -1, -1):
    r[i] = gcd(r[i+1], a[i])

ans = max(l[n-2], r[1])
for i in range(1, n-1):
    ans = max(ans, gcd(l[i-1], r[i+1]))

print(ans)
