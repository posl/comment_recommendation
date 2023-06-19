Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 2

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int,input().split()))
g = a[0]
for i in range(1,n):
    g = gcd(g, a[i])
print(g)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

N = int(input())
A = [int(i) for i in input().split()]
A.sort()
g = A[0]
for i in range(N):
    g = gcd(g, A[i])
print(g)

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

N = input()
A = map(int,raw_input().split())
A.sort()
gcd_num = A[0]
for i in range(1,N):
    gcd_num = gcd(gcd_num,A[i])
print gcd_num

=======
Suggestion 6

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

n=int(input())
a=[int(i) for i in input().split()]
l=[0 for i in range(n)]
r=[0 for i in range(n)]
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
Suggestion 7

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N = int(input())
A = list(map(int, input().split()))

left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(N):
    left[i + 1] = gcd(left[i], A[i])
    right[N - i - 1] = gcd(right[N - i], A[N - i - 1])

ans = 0
for i in range(N):
    ans = max(ans, gcd(left[i], right[i + 1]))

print(ans)

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = [int(x) for x in input().split()]
l = [0] * n
r = [0] * n

l[0] = a[0]
r[n-1] = a[n-1]

for i in range(1, n):
    l[i] = gcd(l[i-1], a[i])
for i in range(n-2, -1, -1):
    r[i] = gcd(r[i+1], a[i])

max_gcd = 0
for i in range(0, n):
    if i == 0:
        max_gcd = max(max_gcd, r[i+1])
    elif i == n-1:
        max_gcd = max(max_gcd, l[i-1])
    else:
        max_gcd = max(max_gcd, gcd(l[i-1], r[i+1]))

print(max_gcd)

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

L = [0] * N
R = [0] * N

L[0] = A[0]
R[N - 1] = A[N - 1]

for i in range(1, N):
    L[i] = gcd(L[i - 1], A[i])

for i in range(N - 2, -1, -1):
    R[i] = gcd(R[i + 1], A[i])

ans = max(L[N - 2], R[1])
for i in range(1, N - 1):
    ans = max(ans, gcd(L[i - 1], R[i + 1]))

print(ans)

=======
Suggestion 10

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
