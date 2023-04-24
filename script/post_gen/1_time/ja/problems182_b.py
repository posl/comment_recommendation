Synthesizing 10/10 solutions

=======
Suggestion 1

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
    if cnt > ans:
        ans = cnt
print(ans)

=======
Suggestion 2

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(2, 1001):
    cnt = 0
    for a in A:
        if a % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        ans_i = i

print(ans_i)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(2, max(a)+1):
    cnt = 0
    for j in range(n):
        if a[j]%i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(2, 1001):
    cnt = 0
    for j in range(N):
        if A[j] % i == 0:
            cnt += 1
    if ans < cnt:
        ans = cnt

print(ans)

=======
Suggestion 5

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x % y
    return x
    
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = 0
max_gcd = 0
for i in range(2, a[0]+1):
    count = 0
    for j in range(n):
        if a[j] % i == 0:
            count += 1
    if count > max_gcd:
        max_gcd = count
        ans = i
        
print(ans)

=======
Suggestion 6

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

n=int(input())
a=[int(i) for i in input().split()]
ans=0
for i in range(2,1001):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans:
        ans=cnt
        ansnum=i
print(ansnum)

=======
Suggestion 7

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(2,max(a)+1):
    cnt = 0
    for j in a:
        if j%i==0:
            cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)

=======
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int,input().split()))
g = a[0]
for i in range(1,n):
    g = gcd(g,a[i])
print(g)

=======
Suggestion 9

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

=======
Suggestion 10

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())

a = list(map(int, input().split()))

gcd_list = [0]*1001

for i in range(2, 1001):
    for j in range(n):
        if a[j] % i == 0:
            gcd_list[i] += 1

print(gcd_list.index(max(gcd_list)))
