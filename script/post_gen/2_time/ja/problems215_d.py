Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 2

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N, M = map(int, input().split())
A = list(map(int, input().split()))

=======
Suggestion 3

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n, m = map(int, input().split())
a = list(map(int, input().split()))

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a

=======
Suggestion 5

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

=======
Suggestion 6

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 7

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

n,m = map(int,input().split())
a = list(map(int,input().split()))

l = [0]*(m+1)
for i in range(n):
    for j in range(1,m+1):
        if gcd(a[i],j) == 1:
            l[j] += 1

ans = []
for i in range(1,m+1):
    if l[i] == n:
        ans.append(i)

print(len(ans))
for i in range(len(ans)):
    print(ans[i])

=======
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
A = list(set(A))
B = [0]*(M+1)
for i in range(len(A)):
    if A[i] == 1:
        continue
    if B[A[i]] == 1:
        continue
    else:
        B[A[i]] = 1
        for j in range(2,M//A[i]+1):
            B[A[i]*j] = 1
ans = []
for i in range(1,M+1):
    if B[i] == 0:
        ans.append(i)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

=======
Suggestion 9

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

N,M = map(int,input().split())
A = list(map(int,input().split()))

L = [True]*(M+1)
for i in A:
    if L[i]:
        for j in range(i,M+1,i):
            L[j] = False

ans = []
for i in range(1,M+1):
    if L[i]:
        ans.append(i)

print(len(ans))
print(*ans,sep="\n")
