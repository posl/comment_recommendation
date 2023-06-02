Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 2

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))

l = [0]*n
r = [0]*n
l[0] = a[0]
r[-1] = a[-1]

for i in range(1, n):
    l[i] = gcd(l[i-1], a[i])
for i in range(n-2, -1, -1):
    r[i] = gcd(r[i+1], a[i])

ans = max(l[-2], r[1])
for i in range(1, n-1):
    ans = max(ans, gcd(l[i-1], r[i+1]))

print(ans)

=======
Suggestion 4

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

n = int(input())
a = list(map(int, input().split()))

l = [0] * n
r = [0] * n
l[0] = a[0]
r[-1] = a[-1]
for i in range(1, n):
    l[i] = gcd(l[i-1], a[i])
    r[n-i-1] = gcd(r[n-i], a[n-i-1])

ans = max(l[n-2], r[1])
for i in range(1, n-1):
    ans = max(ans, gcd(l[i-1], r[i+1]))

print(ans)

=======
Suggestion 5

def gcd(x, y):
    if x < y:
        x, y = y, x
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

=======
Suggestion 6

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

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

ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, r[i+1])
    elif i == n-1:
        ans = max(ans, l[i-1])
    else:
        ans = max(ans, gcd(l[i-1], r[i+1]))

print(ans)

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))

l = [0] * (n + 1)
r = [0] * (n + 1)

for i in range(1, n + 1):
    l[i] = gcd(l[i - 1], a[i - 1])

for i in range(n - 1, -1, -1):
    r[i] = gcd(r[i + 1], a[i])

ans = 0
for i in range(n):
    ans = max(ans, gcd(l[i], r[i + 1]))

print(ans)

=======
Suggestion 8

def gcd(a, b):
    while b != 0:
        a,b = b,a%b
    return a

N = int(input())
A = list(map(int, input().split()))
g = A[0]
for i in range(1, N):
    g = gcd(g, A[i])
print(g)

=======
Suggestion 9

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))
l = [0]*n
r = [0]*n
l[0] = a[0]
r[n-1] = a[n-1]
for i in range(1,n):
    l[i] = gcd(l[i-1],a[i])
    r[n-i-1] = gcd(r[n-i],a[n-i-1])
ans = 1
for i in range(n):
    if i == 0:
        ans = max(ans,r[1])
    elif i == n-1:
        ans = max(ans,l[n-2])
    else:
        ans = max(ans,gcd(l[i-1],r[i+1]))
print(ans)

=======
Suggestion 10

def gcd(a, b):
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
    r[n - 1 - i] = gcd(r[n - i], a[n - 1 - i])

ans = max(l[n - 2], r[1])
for i in range(1, n - 1):
    ans = max(ans, gcd(l[i - 1], r[i + 1]))
print(ans)
