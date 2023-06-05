Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

=======
Suggestion 2

def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    for k in range(2, 1001):
        cnt = 0
        for i in range(n):
            if a[i] % k == 0:
                cnt += 1
        if cnt > ans:
            ans = cnt
            ans_k = k
    print(ans_k)

=======
Suggestion 5

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 6

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
    if tmp > cnt:
        cnt = tmp
        ans = i
print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_gcd = 0
    max_n = 0
    for i in range(2, 1001):
        gcd = 0
        for j in range(n):
            if a[j] % i == 0:
                gcd += 1
        if gcd > max_gcd:
            max_gcd = gcd
            max_n = i
    print(max_n)

=======
Suggestion 8

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in range(2,1001):
    cnt = 0
    for j in range(n):
        if a[j] % i == 0:
            cnt += 1
    if cnt > ans:
        ans = cnt
        ans_num = i
print(ans_num)

=======
Suggestion 9

def gcd(x, y):
    if x < y:
        x, y = y, x
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

N = int(input())
A = list(map(int, input().split()))
max_gcd = 0
max_num = 0
for i in range(2, 1001):
    gcdness = 0
    for a in A:
        if a%i == 0:
            gcdness += 1
    if gcdness > max_gcd:
        max_gcd = gcdness
        max_num = i
print(max_num)
