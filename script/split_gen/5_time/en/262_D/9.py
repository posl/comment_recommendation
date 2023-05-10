def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    # 0～N-1までの整数の2^N-1通りの部分集合のうち、整数平均をとったものが整数になるものの個数を求める
    # 0～N-1までの整数の2^N-1通りの部分集合のうち、整数平均をとったものが整数になるものの個数を求める
    # dp[i][j] = i番目までの要素の部分集合のうち、整数平均をとったものがjになるものの個数
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-A[i-1]]  (j-A[i-1] >= 0)
    dp = [[0 for _ in range(sum(A)+1)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(sum(A)+1):
            dp[i][j] = dp[i-1][j]
            if j-A[i-1] >= 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-A[i-1]]) % MOD
    ans = 0
    for i in range(1, sum(A)+1):
        if i * N in A:
            ans = (ans + dp[N][i]) % MOD
    print(ans)
