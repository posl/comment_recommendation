Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    a.sort(reverse=True)
    dp = [[-float('inf') for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            if j > 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + a[i]*(j-1))
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    print(dp[n][m])

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    dp = [[-float('inf')]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            if j-1>=0:
                dp[i+1][j] = max(dp[i+1][j],dp[i][j-1]+a[i]*(j-1))
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
    print(dp[n][m])
    return

=======
Suggestion 3

def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n):
        for j in range(m+1):
            if j==0:
                dp[i+1][j]=dp[i][j]
            else:
                dp[i+1][j]=max(dp[i][j-1]+a[i]*j,dp[i][j])
    print(dp[n][m])

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(m):
        ans += (i+1)*a[-i-1]
    print(ans)

=======
Suggestion 5

def get_max_sum(n, m, a):
    if n < m:
        return None
    if n == m:
        return sum([i * a[i] for i in range(1, n + 1)])
    else:
        max_sum = 0
        for i in range(n - m + 1):
            tmp_sum = sum([j * a[i + j] for j in range(1, m + 1)])
            if tmp_sum > max_sum:
                max_sum = tmp_sum
        return max_sum

=======
Suggestion 6

def solve(n, m, a):
    dp = [[-float('inf') for i in range(m + 1)] for j in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m + 1):
            if j - 1 >= 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - 1] + (i + 1) * a[i])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    return dp[n][m]

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m + 1):
            if j - 1 >= 0:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - 1] + a[i] * j)
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    print(dp[n][m])

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i] * (j + 1))
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
    print(dp[n][m])

=======
Suggestion 9

def main():
    # input
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    # process
    # dp[i][j] 表示前i个数中选出j个数的最大值
    dp = [[-10**10 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            if j+1<=m:
                dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+a[i]*(j+1))
    # output
    print(max(dp[n]))

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += (i+1)*A[i]
    print(sum)
