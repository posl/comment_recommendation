def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # dp[i][j] := i番目までの数列で、最大値がj以下となる数列の個数
    dp = [[0] * (3001) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(3001):
            # i番目の数を選ばない場合
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= 998244353
            # i番目の数を選ぶ場合
            if A[i] <= j <= B[i]:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= 998244353
    print(sum(dp[N]) % 998244353)
