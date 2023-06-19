Synthesizing 10/10 solutions

=======
Suggestion 1

def max_sum(n, m, a):
    dp = [[-float('inf') for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, min(m+1, i+1)):
            if j == 1:
                dp[i][j] = max(dp[i-1][j], 0) + a[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + j * a[i-1]
    return max(dp[-1])

=======
Suggestion 2

def solve(N, M, A):
    # 求最大值
    # 1. 遍历所有可能的子序列
    # 2. 求子序列的和
    # 3. 求子序列的和的最大值
    # 1. 遍历所有可能的子序列
    # 2. 求子序列的和
    # 3. 求子序列的和的最大值
    # 1. 遍历所有可能的子序列
    # 2. 求子序列的和
    # 3. 求子序列的和的最大值
    # 1. 遍历所有可能的子序列
    # 2. 求子序列的和
    # 3. 求子序列的和的最大值
    # 1. 遍历所有可能的子序列
    # 2. 求子序列的和
    # 3. 求子序列的和的最大值
    # 1. 遍历所有可能的子序列
    # 2. 求子序列的和
    # 3. 求子序列的和的最大值
    # 1. 遍历所有可能的子序列
    # 2. 求子序列的和
    # 3. 求子序列的和的最大值
    # 1. 遍历所有可能的子序列
    # 2. 求子序列的和
    # 3. 求子序列的和的最大值
    # 1. 遍历所有可能的子序列
    # 2. 求子序列的和
    # 3. 求子序列的和的最大值
    # 1. 遍历所有可能的子序列
    # 2. 求子序列的和
    # 3. 求子序列的和的最大值
    # 1

=======
Suggestion 3

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i] * (j + 1))
            if j + 1 < m:
                dp[i + 2][j + 2] = max(dp[i + 2][j + 2], dp[i][j] + a[i] * (j + 1) + a[i + 1] * (j + 2))
    print(dp[n][m])

solve()

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+a[i]*(j+1))
            if i+j+2 <= m:
                dp[i+1][j+2] = max(dp[i+1][j+2],dp[i][j])
    print(dp[n][m])

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[-float('inf') for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = 0
    for i in range(m):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+(i+1)*a[j])
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i+1][j])
    print(dp[m][n])

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            b = a[i:j+1]
            b.sort(reverse=True)
            ans = max(ans, sum(j * b[j] for j in range(len(b))))
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i >= j:
                dp[i][j] = max(dp[i-1][j-1]+i*a[i-1],dp[i-1][j])
    print(dp[n][m])

=======
Suggestion 8

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    dp = [[0 for i in range(M+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = max(dp[i][j+1],dp[i][j]+A[i]*(j+1))
    print(dp[N][M])

=======
Suggestion 9

def max_sum(n,m,a):
    sum = 0
    for i in range(1,m+1):
        sum += i * a[i-1]
    return sum

=======
Suggestion 10

def max_sum(a, m):
    n = len(a)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j]
                if i >= j:
                    dp[i][j] = max(dp[i][j], dp[i - j][j - 1] + j * a[i - 1])
    return dp[n][m]

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(max_sum(a, m))
