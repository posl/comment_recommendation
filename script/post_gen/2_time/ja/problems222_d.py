Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            dp[i + 1][j] += dp[i][j] * max(0, B[i] - A[i] - j + 1)
            dp[i + 1][j] %= mod
            dp[i + 1][j + 1] += dp[i][j] * max(0, B[i] - A[i] - j)
            dp[i + 1][j + 1] %= mod
    print(dp[N][N])

=======
Suggestion 2

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

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    dp = [[0]*3001 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(A[i], B[i]+1):
            dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % MOD
        for j in range(1, 3001):
            dp[i+1][j] = (dp[i+1][j] + dp[i+1][j-1]) % MOD
    print(dp[N][3000])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    dp = [[0] * (B[-1] + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(B[i] + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
            if j < A[i]:
                dp[i + 1][A[i]] += dp[i][j]
                dp[i + 1][A[i]] %= MOD
            else:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
    print(dp[N][-1])

=======
Suggestion 5

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

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    # dp[i][j] = i番目までの数列で、最後の要素がjのときの個数
    dp = [[0] * (3001) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
            dp[i + 1][j] = (dp[i + 1][j] + dp[i + 1][j - 1]) % MOD

    print(dp[N][B[-1]])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] := Aのi番目までの要素を使って、jを作る場合の数
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
    ans = 0
    for i in range(N):
        ans += dp[N][i + 1] * (B[i] - A[i] + 1)
        ans %= MOD
    print(ans)

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    # C[i][j] = (i,j)の範囲のCの個数
    C = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        C[i][i] = 1

    # 逆順に埋めていく
    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N + 1):
            # C[i][j] = C[i][k] * C[k][j]の和
            for k in range(i, j):
                C[i][j] += C[i][k] * C[k][j]
            # A[i] <= C[i][j] <= B[i]になるように調整
            C[i][j] -= C[i][j] - A[i] - B[i]
            C[i][j] %= 998244353

    print(C[0][N])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # DP[i][j] = (i番目まで見て、j以下の数が何個あるか)
    DP = [[0] * (N + 1) for _ in range(N + 1)]
    DP[0][0] = 1
    for i in range(N):
        for j in range(N):
            DP[i + 1][j] += DP[i][j]
            DP[i + 1][j] %= 998244353
            if A[i] <= j <= B[i]:
                DP[i + 1][j + 1] += DP[i][j]
                DP[i + 1][j + 1] %= 998244353
    print(DP[N][N])
