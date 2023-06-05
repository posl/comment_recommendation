Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 1
    for i in range(n):
        ans *= max(0, b[i] - a[i] + 1)
        ans %= 998244353

    print(ans)

=======
Suggestion 2

def countC(a,b):
    result=0
    for i in range(len(a)):
        result+=b[i]-a[i]+1
    return result

=======
Suggestion 3

def problem222_d():
    pass

=======
Suggestion 4

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(n)]
    for i in range(a[0], b[0] + 1):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(a[i], b[i] + 1):
            for k in range(j, b[i - 1] + 1):
                dp[i][j] += dp[i - 1][k]
                dp[i][j] %= mod
    ans = 0
    for i in range(a[-1], b[-1] + 1):
        ans += dp[-1][i]
        ans %= mod
    print(ans)

solve()

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    mod = 998244353
    ans = 1
    for i in range(N):
        ans *= max(0, B[i] - A[i] + 1)
        ans %= mod

    print(ans)

=======
Suggestion 6

def solve1(n, a, b):
    mod = 998244353
    dp = [[0] * 3001 for _ in range(3001)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i] + 1):
            dp[i + 1][j] = dp[i][j] * (j - a[i] + 1) + dp[i + 1][j - 1] * (b[i] - j + 1)
            dp[i + 1][j] %= mod
    return dp[n][b[n - 1]]

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0] * 3001 for _ in range(3001)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dp[i + 1][j] = dp[i + 1][j - 1] + dp[i][j]
            dp[i + 1][j] %= MOD
    print(dp[N][B[N - 1]])

=======
Suggestion 8

def solve(n, a, b):
    # dp[i][j] 表示第i位为j时的数量
    dp = [[0 for j in range(3001)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(a[i-1], b[i-1]+1):
            if i == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = sum(dp[i-1][a[i-2]:j+1]) % 998244353
    return sum(dp[n]) % 998244353

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))

=======
Suggestion 9

def solve(N, A, B):
    MOD = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(A[i-1], B[i-1]+1):
            dp[i][j] = sum(dp[i-1][:j+1]) % MOD
    return sum(dp[N]) % MOD

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(N, A, B))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0] * N
    for i in range(N):
        C[i] = B[i] - A[i] + 1
    for i in range(1, N):
        C[i] *= C[i-1]
        C[i] %= 998244353
    print(C[N-1])
