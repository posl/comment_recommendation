Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(2, 1001):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if cnt < tmp:
        ans = i
        cnt = tmp
print(ans)

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = 0
for i in range(2, 1001):
    c = 0
    for j in a:
        if j % i == 0:
            c += 1
    if c > cnt:
        ans = i
        cnt = c
print(ans)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        r = a % b
        a, b = b, r
    return a

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
cnt = 0

for k in range(2, A[-1]+1):
    c = 0
    for i in range(N):
        if A[i] % k == 0:
            c += 1
    if c > cnt:
        ans = k
        cnt = c

print(ans)

=======
Suggestion 5

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        ans_i = i

print(ans_i)

=======
Suggestion 6

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(2,1001):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if tmp >= ans:
        ans = tmp
        ans_i = i

print(ans_i)

=======
Suggestion 7

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(2,a[-1]+1):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans:
        ans=cnt
        ansnum=i
print(ansnum)

=======
Suggestion 8

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

N = int(input())
A = list(map(int, input().split()))
A.sort()
A.reverse()

max_gcd = 0
max_gcd_num = 0
for i in range(2, A[0] + 1):
    gcd_num = 0
    for j in range(0, N):
        if A[j] % i == 0:
            gcd_num += 1
    if gcd_num > max_gcd:
        max_gcd = gcd_num
        max_gcd_num = i

print(max_gcd_num)

=======
Suggestion 9

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
ans = 0
cnt = 0

for i in range(2, a[0]+1):
    tmp = 0
    for j in range(n):
        if a[j]%i == 0:
            tmp += 1
    if tmp >= cnt:
        ans = i
        cnt = tmp

print(ans)

=======
Suggestion 10

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

GCD = [0] * (A[0]+1)
for i in range(N):
    for j in range(2, A[i]+1):
        if A[i] % j == 0:
            GCD[j] += 1

print(GCD.index(max(GCD)))
