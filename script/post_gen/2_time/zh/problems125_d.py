Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
n=int(input())
a=list(map(int,input().split()))
b=[0]*n
b[0]=a[0]
for i in range(1,n):
    b[i]=gcd(b[i-1],a[i])
print(b[n-1])

=======
Suggestion 2

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 3

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = [int(i) for i in input().split()]
l = [0]*(n+1)
r = [0]*(n+1)
l[0] = a[0]
r[n-1] = a[n-1]
for i in range(1,n):
    l[i] = gcd(l[i-1],a[i])
    r[n-i-1] = gcd(r[n-i],a[n-i-1])
ans = max(l[n-2],r[1])
for i in range(1,n-1):
    ans = max(ans,gcd(l[i-1],r[i+1]))
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

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))
l = [0] * n
r = [0] * n
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
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))
left = [0]*n
right = [0]*n
left[0] = a[0]
right[-1] = a[-1]
for i in range(1,n):
    left[i] = gcd(left[i-1],a[i])
for i in range(n-2,-1,-1):
    right[i] = gcd(right[i+1],a[i])
ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans,right[1])
    elif i == n-1:
        ans = max(ans,left[n-2])
    else:
        ans = max(ans,gcd(left[i-1],right[i+1]))
print(ans)

=======
Suggestion 9

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n=int(input())
a=list(map(int,input().split()))
l=[0]*n
r=[0]*n
l[0]=a[0]
r[n-1]=a[n-1]
for i in range(1,n):
    l[i]=gcd(l[i-1],a[i])
for i in range(n-2,-1,-1):
    r[i]=gcd(r[i+1],a[i])
ans=0
for i in range(n):
    if i==0:
        ans=max(ans,r[1])
    elif i==n-1:
        ans=max(ans,l[n-2])
    else:
        ans=max(ans,gcd(l[i-1],r[i+1]))
print(ans)
