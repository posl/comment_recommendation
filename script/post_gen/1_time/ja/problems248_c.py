Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K + 1):
            for k in range(M + 1):
                if j + k > K:
                    break
                dp[i + 1][j + k] += dp[i][j]
                dp[i + 1][j + k] %= MOD
    print(dp[N][K])

=======
Suggestion 2

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(K + 1):
            for k in range(1, M + 1):
                if j + k <= K:
                    dp[i][j + k] = (dp[i][j + k] + dp[i - 1][j]) % MOD
    print(dp[N][K])

=======
Suggestion 3

def main():
    n, m, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            for l in range(1, m + 1):
                if j - l >= 0:
                    dp[i][j] += dp[i - 1][j - l]
                    dp[i][j] %= 998244353
    print(dp[n][k])

=======
Suggestion 4

def main():
    N, M, K = map(int, input().split())
    MOD = 998244353
    dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(K + 1):
            for k in range(M + 1):
                if j - k >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD
    print(dp[N][K])

=======
Suggestion 5

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0] * (K+1) for i in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(K+1):
            for k in range(1, M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= mod
    print(dp[N][K])

=======
Suggestion 6

def main():
    n, m, k = map(int, input().split())
    ans = 0
    for i in range(1, m+1):
        ans += pow(m, n-1, 998244353) * i * (k-i*n+1) % 998244353
    print(ans%998244353)

=======
Suggestion 7

def main():
    N, M, K = map(int, input().split())
    ans = 0
    for i in range(M):
        ans += (i+1)*pow(M, N-1, 998244353)
    ans *= pow(M, K-N, 998244353)
    print(ans%998244353)

=======
Suggestion 8

def main():
    #入力
    N, M, K = map(int, input().split())

    #初期値
    mod = 998244353
    dp = [[0 for i in range(K+1)] for j in range(N+1)]
    dp[0][0] = 1

    #DP
    for i in range(1, N+1):
        for j in range(1, K+1):
            for k in range(1, M+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]
                    dp[i][j] %= mod

    #出力
    print(dp[N][K])

=======
Suggestion 9

def main():
    N, M, K = map(int, input().split())

    ans = 0
    # Aの1桁目を決める
    for a1 in range(1, M+1):
        # Aの1桁目が決まったときの条件を満たすAの2桁目の個数を数える
        # Aの1桁目がa1のとき、Aの2桁目は1以上M以下の整数である。
        # Aの1桁目がa1のとき、Aの2桁目の個数はM個である。
        # Aの1桁目がa1のとき、Aの2桁目の合計はa1*Mである。
        # Aの1桁目がa1のとき、Aの2桁目の合計がK以下のときのAの2桁目の個数は、
        # K-a1*M以下の整数の個数である。
        # Aの1桁目がa1のとき、Aの2桁目の合計がK以下のときのAの2桁目の個数は、
        # K-a1*M以下の整数の個数は、min(M, K-a1*M)である。
        # Aの1桁目がa1のとき、Aの2桁目の合計がK以下のときのAの2桁目の個数は、
        # min(M, K-a1*M)である。
        # Aの1桁目がa1のとき、Aの2桁目の合計がK以下のときのAの2桁目の個数は、
        # min(M, K-a1*M)である。
        # Aの1桁目がa1のとき、Aの2桁目の合計がK以下のときのAの2桁目の個数は、
        # min(M, K-a1*M)である。
        # Aの1桁

=======
Suggestion 10

def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    # dp[i][j] = A_iまでを使ってjを作る方法の数
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(K + 1):
            for k in range(M + 1):
                if j - k < 0:
                    break
                dp[i][j] += dp[i - 1][j - k]
                dp[i][j] %= mod
    print(dp[N][K])
