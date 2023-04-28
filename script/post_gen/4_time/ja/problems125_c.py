Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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

ans = max(r[1], l[n - 2])

for i in range(1, n - 1):
    ans = max(ans, gcd(l[i - 1], r[i + 1]))

print(ans)

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

n = int(input())
a = list(map(int, input().split()))
l = [0] * (n+1)
r = [0] * (n+1)

for i in range(n):
    l[i+1] = gcd(l[i], a[i])
    r[n-i-1] = gcd(r[n-i], a[n-i-1])

ans = 0
for i in range(n):
    ans = max(ans, gcd(l[i], r[i+1]))

print(ans)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))

left = [0] * n
right = [0] * n
left[0] = a[0]
right[n-1] = a[n-1]
for i in range(1, n):
    left[i] = gcd(left[i-1], a[i])
    right[n-i-1] = gcd(right[n-i], a[n-i-1])

ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, right[1])
    elif i == n-1:
        ans = max(ans, left[n-2])
    else:
        ans = max(ans, gcd(left[i-1], right[i+1]))

print(ans)

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

l = [0 for i in range(n)]
r = [0 for i in range(n)]

l[0] = a[0]
r[n-1] = a[n-1]

for i in range(1, n):
    l[i] = gcd(l[i-1], a[i])
    r[n-1-i] = gcd(r[n-i], a[n-1-i])

ans = max(l[n-2], r[1])

for i in range(1, n-1):
    ans = max(ans, gcd(l[i-1], r[i+1]))

print(ans)

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))

left = [0] * (n + 1)
right = [0] * (n + 1)

for i in range(n):
    left[i+1] = gcd(left[i],a[i])

for i in range(n-1,-1,-1):
    right[i] = gcd(right[i+1],a[i])

ans = 1
for i in range(n):
    ans = max(ans,gcd(left[i],right[i+1]))

print(ans)

=======
Suggestion 8

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int,input().split()))

ans = 0
for i in range(n):
    ans = gcd(ans, a[i])

print(ans)

=======
Suggestion 9

def gcd(n, m):
    n, m = max(n, m), min(n, m)
    if m == 0:
        return n
    return gcd(m, n % m)

n = int(input())
a = list(map(int, input().split()))
a.sort()

cnt = 0
for i in range(n):
    cnt = gcd(cnt, a[i])

print(cnt)

=======
Suggestion 10

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))
a.sort()

max_gcd = 0
for i in range(n-1):
    max_gcd = gcd(max_gcd,a[i+1]-a[i])

print(max_gcd)
