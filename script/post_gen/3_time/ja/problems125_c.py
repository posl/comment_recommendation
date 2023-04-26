Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

N = int(input())
A = [int(x) for x in input().split()]
A.sort()

ans = 0
for i in range(N):
    ans = gcd(ans, A[i])
print(ans)

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n=int(input())
a=list(map(int,input().split()))

=======
Suggestion 3

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
r[n-1] = a[n-1]

for i in range(1,n):
    l[i] = gcd(l[i-1], a[i])

for i in range(n-2,-1,-1):
    r[i] = gcd(r[i+1], a[i])

ans = max(l[n-2], r[1])
for i in range(1,n-1):
    ans = max(ans, gcd(l[i-1], r[i+1]))

print(ans)

=======
Suggestion 4

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(input())
a = list(map(int, input().split()))

l = [0] * n
r = [0] * n
l[0] = a[0]
r[-1] = a[-1]
for i in range(1, n):
    l[i] = gcd(l[i-1], a[i])
    r[n-i-1] = gcd(r[n-i], a[n-i-1])

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
Suggestion 5

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

N = int(input())
A = list(map(int, input().split()))

=======
Suggestion 6

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

n=int(input())
a=list(map(int,input().split()))
l=[0]*(n+1)
r=[0]*(n+1)
for i in range(n):
    l[i+1]=gcd(l[i],a[i])
    r[n-i-1]=gcd(r[n-i],a[n-i-1])
ans=0
for i in range(n):
    ans=max(ans,gcd(l[i],r[i+1]))
print(ans)

=======
Suggestion 7

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

N = int(input())
A = list(map(int,input().split()))

L = [0] * (N+1)
R = [0] * (N+1)

L[0] = A[0]
R[N-1] = A[N-1]

for i in range(1,N):
    L[i] = gcd(L[i-1],A[i])
    R[N-i-1] = gcd(R[N-i],A[N-i-1])

ans = 0

for i in range(N):
    if i == 0:
        ans = max(ans,R[i+1])
    elif i == N-1:
        ans = max(ans,L[i-1])
    else:
        ans = max(ans,gcd(L[i-1],R[i+1]))

print(ans)

=======
Suggestion 8

def get_gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 9

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
n = int(input())
a = list(map(int,input().split()))
left = [0]*(n+1)
right = [0]*(n+1)
for i in range(n):
    left[i+1] = gcd(left[i],a[i])
for i in range(n-1,-1,-1):
    right[i] = gcd(right[i+1],a[i])
ans = 0
for i in range(n):
    ans = max(ans,gcd(left[i],right[i+1]))
print(ans)

=======
Suggestion 10

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

N=int(input())
A=list(map(int,input().split()))
gcd_max=0
for i in range(N):
    gcd_max=gcd(gcd_max,A[i])
print(gcd_max)
