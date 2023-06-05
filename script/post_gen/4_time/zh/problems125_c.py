Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))
l = [0] * n
r = [0] * n
l[0] = a[0]
r[n-1] = a[n-1]
for i in range(1,n):
    l[i] = gcd(l[i-1],a[i])
    r[n-i-1] = gcd(r[n-i],a[n-i-1])
ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans,r[i+1])
    elif i == n-1:
        ans = max(ans,l[i-1])
    else:
        ans = max(ans,gcd(l[i-1],r[i+1]))
print(ans)

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 3

def gcd(x,y):
    if x<y:
        x,y=y,x
    if y==0:
        return x
    return gcd(y,x%y)

n=int(input())
a=list(map(int,input().split()))
l=[0]*n
r=[0]*n

l[0]=a[0]
r[-1]=a[-1]
for i in range(1,n):
    l[i]=gcd(l[i-1],a[i])
for i in range(n-2,-1,-1):
    r[i]=gcd(r[i+1],a[i])

ans=0
for i in range(n):
    if i==0:
        ans=max(ans,r[i+1])
    elif i==n-1:
        ans=max(ans,l[i-1])
    else:
        ans=max(ans,gcd(l[i-1],r[i+1]))
print(ans)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

=======
Suggestion 5

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n=int(input())
a=list(map(int,input().split()))

l=[0]*(n+1)
r=[0]*(n+1)

for i in range(n):
    l[i+1]=gcd(l[i],a[i])

for i in range(n-1,-1,-1):
    r[i]=gcd(r[i+1],a[i])

ans=0
for i in range(n):
    ans=max(ans,gcd(l[i],r[i+1]))
print(ans)

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N = int(input())
A = list(map(int, input().split()))

left = [0] * N
right = [0] * N

left[0] = A[0]
right[N-1] = A[N-1]

for i in range(1, N):
    left[i] = gcd(left[i-1], A[i])

for i in range(N-2, -1, -1):
    right[i] = gcd(right[i+1], A[i])

ans = 0
for i in range(N):
    if i == 0:
        ans = max(ans, right[1])
    elif i == N-1:
        ans = max(ans, left[N-2])
    else:
        ans = max(ans, gcd(left[i-1], right[i+1]))

print(ans)

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    while b > 0:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]
l[0] = a[0]
r[n - 1] = a[n - 1]
for i in range(1, n):
    l[i] = gcd(l[i - 1], a[i])
    r[n - i - 1] = gcd(r[n - i], a[n - i - 1])
ans = max(l[n - 2], r[1])
for i in range(1, n - 1):
    ans = max(ans, gcd(l[i - 1], r[i + 1]))
print(ans)

=======
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))
l = [0]*(n+1)
r = [0]*(n+1)
for i in range(n):
    l[i+1] = gcd(l[i],a[i])
    r[n-i-1] = gcd(r[n-i],a[n-i-1])
ans = 0
for i in range(n):
    ans = max(ans,gcd(l[i],r[i+1]))
print(ans)
