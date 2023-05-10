def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # dp[i][j] = i番目までの要素を使って、j番目の数値を作ることが出来る通り数
    dp = [[0] * 3001 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(3001):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= 998244353
            if A[i] <= j and j <= B[i]:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= 998244353
    print(dp[N][B[N - 1]])
