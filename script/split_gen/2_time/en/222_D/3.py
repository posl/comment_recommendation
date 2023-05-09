def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0 for i in range(3001)] for j in range(N)]
    dp[0][A[0]:B[0]+1] = [1 for i in range(A[0], B[0]+1)]
    for i in range(1, N):
        for j in range(3001):
            if j < A[i]:
                dp[i][j] = 0
            elif j > B[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = sum(dp[i-1][A[i]:j+1]) % MOD
    print(sum(dp[N-1]) % MOD)
