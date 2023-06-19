Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N = int(input())
A = list(map(int, input().split()))

ans = 0
max_gcd = 0

for i in range(2, 1001):
    cnt = 0
    for j in range(N):
        if A[j]%i == 0:
            cnt += 1
    if cnt > max_gcd:
        max_gcd = cnt
        ans = i

print(ans)

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 3

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()

ans = 0
cnt = 0
for i in range(2, a[0]+1):
    c = 0
    for j in range(n):
        if a[j] % i == 0:
            c += 1
    if cnt < c:
        cnt = c
        ans = i

print(ans)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

n = int(input())
a = list(map(int, input().split()))

ans = 0
max = 0
for k in range(2, 1001):
    cnt = 0
    for i in a:
        if i%k == 0:
            cnt += 1
    if cnt > max:
        ans = k
        max = cnt

print(ans)

=======
Suggestion 5

def gcd(n, m):
    if n < m:
        n, m = m, n
    while m != 0:
        n, m = m, n % m
    return n

=======
Suggestion 6

def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())
a = list(map(int, input().split()))
ans = 0
max_gcdness = 0
for i in range(2, 1001):
    gcdness = 0
    for j in range(n):
        if a[j] % i == 0:
            gcdness += 1
    if max_gcdness < gcdness:
        max_gcdness = gcdness
        ans = i
print(ans)

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
cnt = 0

for i in range(2, 1001):
    temp = 0
    for j in range(n):
        if a[j] % i == 0:
            temp += 1
    if cnt < temp:
        ans = i
        cnt = temp

print(ans)

=======
Suggestion 8

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

=======
Suggestion 9

def gcd(a,b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
ans = 0
cnt = 0
for i in range(2,1001):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if tmp > cnt:
        cnt = tmp
        ans = i
print(ans)
