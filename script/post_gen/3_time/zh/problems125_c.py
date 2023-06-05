Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))
g = A[0]
for i in range(1, N):
    g = gcd(g, A[i])
print(g)

=======
Suggestion 2

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
ans = max(l[n-2],r[1])
for i in range(1,n-1):
    ans = max(ans,gcd(l[i-1],r[i+1]))
print(ans)

=======
Suggestion 3

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n=int(input())
a=list(map(int,input().split()))
l=[0]*n
r=[0]*n
l[0]=a[0]
r[n-1]=a[n-1]
for i in range(1,n):
    l[i]=gcd(l[i-1],a[i])
    r[n-1-i]=gcd(r[n-i],a[n-1-i])
ans=max(l[n-2],r[1])
for i in range(1,n-1):
    ans=max(ans,gcd(l[i-1],r[i+1]))
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

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))
A.sort()
A.reverse()
# print(A)

B = [0] * N
B[0] = A[0]
for i in range(1, N):
    B[i] = gcd(B[i-1], A[i])
# print(B)
print(B[N-1])

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(N):
    left[i + 1] = gcd(left[i], A[i])
    right[N - i - 1] = gcd(right[N - i], A[N - i - 1])

ans = 1
for i in range(N):
    ans = max(ans, gcd(left[i], right[i + 1]))

print(ans)

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))
ans = a[0]
for i in range(1, n):
    ans = gcd(ans, a[i])
print(ans)

=======
Suggestion 8

def gcd(a,b):
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
ans=max(l[n-2],r[1])
for i in range(1,n-1):
    ans=max(ans,gcd(l[i-1],r[i+1]))
print(ans)

=======
Suggestion 9

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
    r[n-1-i] = gcd(r[n-i], a[n-1-i])

ans = 1
for i in range(n):
    ans = max(ans, gcd(l[i], r[i+1]))

print(ans)
