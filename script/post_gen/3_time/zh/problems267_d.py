Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append((abs(a[i]), a[i]))
    b.sort(reverse=True)
    ans = 0
    for i in range(m):
        ans += b[i][1]
    print(ans)

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum += (i+1+j)*a[i+j]
        ans = max(ans,sum)
    print(ans)

=======
Suggestion 3

def max_sum(a, n, m):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j > i:
                dp[i][j] = -1000000000
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + a[i-1]*(j-1))
    ans = -1000000000
    for i in range(1, n+1):
        ans = max(ans, dp[i][m] + a[i-1]*m)
    return ans

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[-10**9 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+1 <= m:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + (i+1)*a[i])
    print(dp[n][m])

=======
Suggestion 5

def get_max_sum(n,m,nums):
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+i*nums[i-1])
    return dp[n][m]

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[-float("inf")] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]
            if i - j >= 0:
                dp[i][j] = max(dp[i][j], dp[i - j][j - 1] + a[i - 1] * j)
    print(dp[n][m])

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-m+1):
        ans = max(ans, sum([(i+1)*a[i] for i in range(i, i+m)]))
    print(ans)

=======
Suggestion 8

def max_sum():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+i*a[i-1])
    print(dp[n][m])

=======
Suggestion 9

def solve():
    pass

=======
Suggestion 10

def solve(n,m,a):
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+i*a[i-1])
    print(dp[n][m])
