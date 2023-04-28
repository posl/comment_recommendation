Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

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
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    return gcd(y, x % y)

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

max_gcd = 0
for i in range(2, 1001):
    count = 0
    for j in range(n):
        if a[j] % i == 0:
            count += 1
    if count > max_gcd:
        max_gcd = count
        ans = i

print(ans)

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
cnt = 0
for i in range(2, 1001):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if tmp >= cnt:
        cnt = tmp
        ans = i

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

ans = 0
cnt = 0
for i in range(2, 1001):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if cnt < tmp:
        cnt = tmp
        ans = i
print(ans)

=======
Suggestion 7

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))

ans = 0
for i in range(2,1001):
    cnt = 0
    for j in range(n):
        if a[j]%i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        ans2 = i
print(ans2)

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
gcdness = [0] * (a[0] + 1)

for i in range(n):
    for j in range(2, a[i] + 1):
        if gcdness[j] == 1:
            continue
        if a[i] % j == 0:
            gcdness[j] += 1
            k = j + j
            while k <= a[0]:
                gcdness[k] = 1
                k += j

ans = 0
for i in range(2, a[0] + 1):
    if gcdness[i] > 1:
        ans = i

print(ans)

=======
Suggestion 9

def gcd(a,b):
    while b:
        a,b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0
cnt = 0
for i in range(2,a[-1]+1):
    tmp = 0
    for j in range(n):
        if a[j] % i == 0:
            tmp += 1
    if tmp > cnt:
        cnt = tmp
        ans = i

print(ans)
