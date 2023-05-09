def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(N)]
    for i in range(A[0], B[0] + 1):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(1, 3001):
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD
    ans = 0
    for i in range(A[-1], B[-1] + 1):
        ans = (ans + dp[N - 1][i]) % MOD
    print(ans)
