Synthesizing 10/10 solutions

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
max_gcd = 0
for i in range(2, a[0]+1):
    cnt = 0
    for j in a:
        if j % i == 0:
            cnt += 1
    if cnt > max_gcd:
        ans = i
        max_gcd = cnt
print(ans)

=======
Suggestion 2

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

n=int(input())
a=list(map(int,input().split()))
ans=0
ans_n=0
for i in range(2,1001):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans_n:
        ans_n=cnt
        ans=i
print(ans)

=======
Suggestion 3

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

n=int(input())
a=list(map(int,input().split()))
ans=0
ans_gcd=0
for i in range(2,1001):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans:
        ans=cnt
        ans_gcd=i
print(ans_gcd)

=======
Suggestion 4

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)

=======
Suggestion 5

def gcd(a,b):
  if b == 0: return a
  return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(2,1001):
  tmp = 0
  for j in range(n):
    if a[j]%i == 0: tmp += 1
  if tmp >= ans:
    ans = tmp
    ans_num = i

print(ans_num)

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))
ans = 0
ans_num = 0

for i in range(2, 1001):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if tmp > ans:
        ans = tmp
        ans_num = i

print(ans_num)

=======
Suggestion 8

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

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
        res=i
print(res)

=======
Suggestion 9

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x%y)

n = int(input())
a = list(map(int, input().split()))

ans = 0
cnt = 0
for i in range(2, 1001):
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

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(2, max(A) + 1):
    cnt = 0
    for j in A:
        if j % i == 0:
            cnt += 1
    if cnt >= ans:
        ans = cnt
        num = i
print(num)
