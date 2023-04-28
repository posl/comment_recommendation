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

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in a:
        if j % i == 0:
            cnt += 1
    if ans < cnt:
        ans = cnt
        ans_i = i

print(ans_i)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in range(N):
        if A[j] % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)

=======
Suggestion 4

def gcd(a,b):
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
    
n = int(input())
a = list(map(int, input().split()))

ans = 0

for i in range(2, 1001):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if ans < tmp:
        ans = tmp

print(ans)

=======
Suggestion 6

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

n = int(input())
a = list(map(int,input().split()))

ans = 0
for i in range(2, max(a)+1):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)

=======
Suggestion 7

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a

    return gcd(b, a % b)


n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(2, 1001):
    tmp = 0
    for j in a:
        if j % i == 0:
            tmp += 1
    if tmp > ans:
        ans = tmp

print(ans)

=======
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

N = int(input())
A = list(map(int,input().split()))

ans = 0
for k in range(2,1001):
    cnt = 0
    for i in range(N):
        if A[i]%k == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)

=======
Suggestion 9

def gcd(a, b):
    if a%b==0:
        return(b)
    else:
        return(gcd(b, a%b))

n=int(input())
a=list(map(int, input().split()))
ans=0
for i in range(2, max(a)+1):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans:
        ans=cnt
        ans2=i
print(ans2)

=======
Suggestion 10

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

N = int(input())
A = list(map(int,input().split()))

max_gcd = 0
for i in range(N):
    tmp_gcd = 0
    for j in range(N):
        if i == j:
            continue
        tmp_gcd = gcd(tmp_gcd, A[j])
    max_gcd = max(max_gcd, tmp_gcd)
print(max_gcd)
