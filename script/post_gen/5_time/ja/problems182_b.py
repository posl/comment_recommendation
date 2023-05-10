Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

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
ans=0
for i in range(2,1001):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans:
        ans=cnt
print(ans)

=======
Suggestion 3

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

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

print(ans)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a

n = int(input())
a = list(map(int, input().split()))

ans = 0
for k in range(2, max(a)+1):
    cnt = 0
    for i in range(n):
        if a[i] % k == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)

=======
Suggestion 5

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in range(n):
        if a[j]%i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)

=======
Suggestion 6

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if ans < cnt:
        ans = cnt
        ans_i = i

print(ans_i)

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

ans = 0
max_gcd = 0
for i in range(2, 1001):
    gcd_cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            gcd_cnt += 1
    if gcd_cnt > max_gcd:
        max_gcd = gcd_cnt
        ans = i

print(ans)

=======
Suggestion 8

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(2,1001):
    cnt=0
    for j in a:
        if j%i==0:
            cnt+=1
    if cnt>ans:
        ans=cnt
print(ans)

=======
Suggestion 9

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in a:
        if j % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)

=======
Suggestion 10

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(2,1001):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans:
        ans=cnt
print(ans)
