Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))

l = [0] * n
r = [0] * n

for i in range(1, n):
    l[i] = gcd(l[i - 1], a[i - 1])
    r[n - i - 1] = gcd(r[n - i], a[n - i])

ans = 0
for i in range(n):
    ans = max(ans, gcd(l[i], r[i]))

print(ans)

=======
Suggestion 2

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
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
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

left = [0] * N
right = [0] * N
left[0] = A[0]
right[N - 1] = A[N - 1]

for i in range(1, N):
    left[i] = gcd(left[i - 1], A[i])

for i in range(N - 2, -1, -1):
    right[i] = gcd(right[i + 1], A[i])

ans = 0
for i in range(N):
    if i == 0:
        ans = max(ans, right[1])
    elif i == N - 1:
        ans = max(ans, left[N - 2])
    else:
        ans = max(ans, gcd(left[i - 1], right[i + 1]))

print(ans)

=======
Suggestion 4

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
A = list(map(int, input().split()))
L = [0] * N
R = [0] * N
L[0] = A[0]
R[N-1] = A[N-1]
for i in range(1, N):
    L[i] = gcd(L[i-1], A[i])
for i in range(N-2, -1, -1):
    R[i] = gcd(R[i+1], A[i])
ans = max(L[N-2], R[1])
for i in range(1, N-1):
    ans = max(ans, gcd(L[i-1], R[i+1]))
print(ans)

=======
Suggestion 5

def gcd(a, b):
    while b: a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))

l = [0] * (n + 1)
r = [0] * (n + 1)

for i in range(n):
    l[i + 1] = gcd(l[i], a[i])
    r[n - i - 1] = gcd(r[n - i], a[n - i - 1])

ans = 0
for i in range(n):
    ans = max(ans, gcd(l[i], r[i + 1]))

print(ans)

=======
Suggestion 6

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))

left = [0]*n
right = [0]*n

left[0] = a[0]
right[n-1] = a[n-1]

for i in range(1, n):
    left[i] = gcd(left[i-1], a[i])
    right[n-1-i] = gcd(right[n-i], a[n-1-i])

ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans, right[i+1])
    elif i == n-1:
        ans = max(ans, left[i-1])
    else:
        ans = max(ans, gcd(left[i-1], right[i+1]))

print(ans)

=======
Suggestion 7

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

n=int(input())
a=list(map(int,input().split()))

l=[0]*n
r=[0]*n
l[0]=a[0]
r[n-1]=a[n-1]

for i in range(1,n):
    l[i]=gcd(l[i-1],a[i])
    r[n-i-1]=gcd(r[n-i],a[n-i-1])

ans=1
for i in range(n):
    if i==0:
        ans=max(ans,r[1])
    elif i==n-1:
        ans=max(ans,l[n-2])
    else:
        ans=max(ans,gcd(l[i-1],r[i+1]))
print(ans)

=======
Suggestion 8

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

N = int(input())
A = list(map(int, input().split()))

left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(1, N + 1):
    left[i] = gcd(left[i - 1], A[i - 1])

for i in range(N - 1, -1, -1):
    right[i] = gcd(right[i + 1], A[i])

ans = 0
for i in range(N):
    ans = max(ans, gcd(left[i], right[i + 1]))
print(ans)

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n=int(input())
a=list(map(int,input().split()))
b=[0]*n
c=[0]*n
b[0]=a[0]
c[n-1]=a[n-1]
for i in range(1,n):
    b[i]=gcd(b[i-1],a[i])
    c[n-1-i]=gcd(c[n-i],a[n-1-i])
max=0
for i in range(n):
    if i==0:
        if max<b[i+1]:
            max=b[i+1]
    elif i==n-1:
        if max<c[i-1]:
            max=c[i-1]
    else:
        if max<gcd(b[i-1],c[i+1]):
            max=gcd(b[i-1],c[i+1])
print(max)

=======
Suggestion 10

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

gcd_max = 0
gcd_list = [0 for _ in range(N)]
gcd_list[0] = A[0]
gcd_list[N - 1] = A[N - 1]

for i in range(1, N):
    gcd_list[i] = gcd(gcd_list[i - 1], A[i])
gcd_max = max(gcd_max, gcd_list[N - 2])

for i in range(N - 1, 0, -1):
    gcd_list[i] = gcd(gcd_list[i + 1], A[i])
gcd_max = max(gcd_max, gcd_list[1])

for i in range(1, N - 1):
    gcd_max = max(gcd_max, gcd(gcd_list[i - 1], gcd_list[i + 1]))

print(gcd_max)
