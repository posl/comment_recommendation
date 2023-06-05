def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2**N通りの操作の結果を求める
    # dp[i][j] := i番目までの数字を使って、最後の数字をjにする方法の数
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[0][A[0]] = 1
    for i in range(N - 1):
        for j in range(10):
            dp[i + 1][(j + A[i + 1]) % 10] += dp[i][j]
            dp[i + 1][(j + A[i + 1]) % 10] %= 998244353
            dp[i + 1][(j * A[i + 1]) % 10] += dp[i][j]
            dp[i + 1][(j * A[i + 1]) % 10] %= 998244353
    # 出力
    for i in range(10):
        print(dp[N - 1][i])

if __name__ == '__main__':
    main()