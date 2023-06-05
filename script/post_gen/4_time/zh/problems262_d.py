Synthesizing 10/10 solutions

=======
Suggestion 1

def f(n):
    if n == 1:
        return 1
    return f(n-1) + 2**(n-1)

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n+1):
    for j in range(n-i+1):
        if sum(a[j:j+i]) % i == 0:
            ans += 1
print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 998244353
    sumA = sum(A)
    dp = [[0 for _ in range(sumA+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(sumA+1):
            if j-A[i]>=0:
                dp[i+1][j] = (dp[i][j]+dp[i][j-A[i]])%mod
            else:
                dp[i+1][j] = dp[i][j]
    ans = 0
    for i in range(1, sumA+1):
        if i%N==0:
            ans = (ans+dp[N][i])%mod
    print(ans)

=======
Suggestion 3

def solve():
    #n = int(input())
    #a = list(map(int,input().split()))
    n = 5
    a = [5,5,5,5,5]
    ans = 0
    for i in range(1,2**n):
        sum = 0
        cnt = 0
        for j in range(n):
            if (i>>j)&1:
                sum += a[j]
                cnt += 1
        if sum%cnt == 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def countAverage(n, a):
    sum = 0
    for i in range(n):
        sum += a[i]
    if sum % n == 0:
        return True
    else:
        return False

=======
Suggestion 5

def get_count(N, A):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (A[i]+A[j])%2 == 0:
                count += 1
    return count

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i,n):
            if sum(a[i:j+1]) % (j-i+1) == 0:
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        for j in range(i,n):
            if sum(a[i:j+1]) % (j-i+1) == 0:
                cnt += 1
    print(cnt)

=======
Suggestion 8

def func(a):
    return sum(a) % len(a) == 0

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(2**n - 1):
    b = []
    for j in range(n):
        if i >> j & 1:
            b.append(a[j])
    if func(b):
        ans += 1
print(ans)

=======
Suggestion 9

def getNumOfIntAvg(nums):
    n = len(nums)
    # dp[i][j]表示前i个数中，选出j个数，这些数的和为i的情况数
    dp = [[0 for i in range(n+1)] for j in range(sum(nums)+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(sum(nums)+1):
            dp[j][i+1] += dp[j][i]
            if j >= nums[i]:
                dp[j][i+1] += dp[j-nums[i]][i]
    res = 0
    for i in range(1, sum(nums)+1):
        if i % n == 0:
            res += dp[i][n]
    return res

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if (A[i]+A[j])%2==0 and (A[i]+A[j])//2 in A:
                ans += 1
    print(ans)
