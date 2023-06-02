Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    ans_n = 0
    for i in range(2, 1001):
        tmp = 0
        for j in range(n):
            if a[j] % i == 0:
                tmp += 1
        if tmp >= ans_n:
            ans_n = tmp
            ans = i
    print(ans)

=======
Suggestion 2

def gcd(a, b): # a > b
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
ans = 1
for i in range(2, 1001):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt >= ans:
        ans = i
print(ans)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
ans = 0
ans_gcd = 0
for i in range(2, 1001):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        ans_gcd = i
print(ans_gcd)

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
ans_cnt = 0
for i in range(2, a[0] + 1):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt > ans_cnt:
        ans_cnt = cnt
        ans = i
print(ans)

=======
Suggestion 6

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

=======
Suggestion 7

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
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans:
        ans=cnt
        ans2=i
print(ans2)

=======
Suggestion 8

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

=======
Suggestion 9

def gcd(x, y):
    if x < y:
        x, y = y, x
    while y > 0:
        x, y = y, x%y
    return x

n = int(input())
a = list(map(int, input().split()))
ans = 0
cnt = 0
for k in range(2, 1001):
    c = 0
    for i in range(n):
        if a[i] % k == 0:
            c += 1
    if cnt < c:
        cnt = c
        ans = k
print(ans)

=======
Suggestion 10

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
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        res = i
print(res)
