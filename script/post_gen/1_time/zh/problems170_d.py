Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = max(A)
    count = [0 for i in range(maxA+1)]
    for a in A:
        count[a] += 1
    ans = 0
    for a in A:
        if count[a] == 1:
            ans += 1
    print(ans)
solve()

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    cnt = 0
    for i in range(1, N):
        if A[i] % A[i-1] == 0:
            cnt += 1
    print(N - cnt - 1)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    dp = [0]*n
    dp[0] = 1
    for i in range(1,n):
        if a[i] == a[i-1]:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + 1
    print(n-dp[-1])

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    # 从小到大排序
    a.sort()
    # 用于记录数字i是否为满足条件的数字
    ans = [True for i in range(n)]
    # 从小到大遍历
    for i in range(n):
        # 如果数字i已经被标记为不满足条件的数字，则跳过
        if not ans[i]:
            continue
        # 从小到大遍历
        for j in range(i + 1, n):
            # 如果数字j已经被标记为不满足条件的数字，则跳过
            if not ans[j]:
                continue
            # 如果数字j可以被数字i整除，则标记数字j为不满足条件的数字
            if a[j] % a[i] == 0:
                ans[j] = False

    # 计数满足条件的数字个数
    cnt = 0
    for i in range(n):
        if ans[i]:
            cnt += 1
    print(cnt)

=======
Suggestion 5

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            if A[j] % A[i] == 0:
                B[i] += 1
    ans = 0
    for i in range(N):
        if B[i] == 0:
            ans += 1
    print(ans)

=======
Suggestion 7

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
n = int(input())
a = list(map(int,input().split()))
a.sort()
b = [0]*n
c = [0]*n
for i in range(n):
    b[i] = a[i]
    c[i] = a[i]
for i in range(n-2,-1,-1):
    b[i] = gcd(b[i],b[i+1])
for i in range(1,n):
    c[i] = gcd(c[i],c[i-1])
ans = 1
for i in range(n):
    if i == 0:
        if a[i] % b[i+1] != 0:
            ans += 1
    elif i == n-1:
        if a[i] % c[i-1] != 0:
            ans += 1
    else:
        if gcd(b[i+1],c[i-1]) == 1:
            ans += 1
print(ans)

=======
Suggestion 8

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
a = list(map(int, input().split()))

left = [0] * n
right = [0] * n

left[0] = a[0]
right[n - 1] = a[n - 1]

for i in range(1, n):
    left[i] = gcd(left[i - 1], a[i])

for i in range(n - 2, -1, -1):
    right[i] = gcd(right[i + 1], a[i])

ans = 1
for i in range(n):
    if i == 0:
        tmp = right[1]
    elif i == n - 1:
        tmp = left[n - 2]
    else:
        tmp = gcd(left[i - 1], right[i + 1])
    ans = max(ans, tmp)

print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 1
    for i in range(1, n):
        if a[i] % a[i-1] != 0:
            cnt += 1
    print(cnt)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        if i == 0:
            if a[i] != a[i+1]:
                cnt += 1
        elif i == n-1:
            if a[i] != a[i-1]:
                cnt += 1
        else:
            if a[i] != a[i-1] and a[i] != a[i+1]:
                cnt += 1
    print(cnt)
