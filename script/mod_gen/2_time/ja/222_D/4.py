def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    # DPテーブル
    # dp[i][j] := i番目までの数列のうち、最後の要素がjのものの個数
    dp = [[0] * (3001) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        # 累積和
        sum = [0] * (3001)
        for j in range(3001):
            if j == 0:
                sum[j] = dp[i][j]
            else:
                sum[j] = (sum[j-1] + dp[i][j]) % MOD
        for j in range(A[i], B[i]+1):
            dp[i+1][j] = (sum[j] - sum[A[i]-1]) % MOD
    ans = 0
    for i in range(3001):
        ans = (ans + dp[N][i]) % MOD
    print(ans)

if __name__ == '__main__':
    main()