Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 2

def gcd(a, b):
    if a<b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in a:
        if j%i==0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        res = i
print(res)

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
ans_num = 0
for k in range(2, 1001):
    cnt = 0
    for i in range(N):
        if A[i] % k == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        ans_num = k

print(ans_num)

=======
Suggestion 4

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

=======
Suggestion 5

def gcd(a, b):
    if a<b:
        a,b=b,a
    while b:
        a,b=b,a%b
    return a

n=int(input())
a=list(map(int, input().split()))
max_gcd=0
ans=0
for i in range(2, 1001):
    cnt=0
    for j in range(n):
        if gcd(a[j], i)==i:
            cnt+=1
    if cnt>=max_gcd:
        max_gcd=cnt
        ans=i
print(ans)

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
gcdness = 0
ans = 0
for i in range(2, a[0]+1):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt > gcdness:
        gcdness = cnt
        ans = i
print(ans)

=======
Suggestion 7

def gcd(x,y):
    if x<y:
        x,y=y,x
    while y!=0:
        x,y=y,x%y
    return x

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n = int(input())
a = [int(i) for i in input().split()]
ans = 0
for i in range(2, 1001):
    cnt = 0
    for j in a:
        if j % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        ans_num = i
print(ans_num)

=======
Suggestion 9

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))

max_gcd = 0
for i in range(2,1001):
    gcdness = 0
    for j in range(n):
        if a[j]%i == 0:
            gcdness += 1
    if gcdness > max_gcd:
        max_gcd = gcdness
        ans = i

print(ans)
