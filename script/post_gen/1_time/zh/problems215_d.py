Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
ans.append(1)
for i in range(2,m+1):
    flag=0
    for j in range(n):
        if gcd(a[j],i)!=1:
            flag=1
            break
    if flag==0:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)

=======
Suggestion 2

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

N, M = map(int, input().split())
A = list(map(int, input().split()))

max_A = max(A)
max_M = max(M, max_A)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 4

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A = list(set(A))

ans = 0
for i in range(1, M + 1):
    flag = True
    for j in range(len(A)):
        if gcd(A[j], i) != 1:
            flag = False
            break
    if flag:
        ans += 1
        print(i)

print(ans)

=======
Suggestion 6

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 8

def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y,x%y)

=======
Suggestion 9

def gcd(m,n):
    if m<n:
        m,n=n,m
    if n==0:
        return m
    else:
        return gcd(n,m%n)
