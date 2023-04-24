Synthesizing 8/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    MOD = 10**9+7

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    dp[0][0] = 1
    for i in range(1, K+1):
        for j in range(1, N+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) % mod
    for i in range(1, K+1):
        print((dp[i][N] - dp[i-1][N]) % mod)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7

    # K個の青いボールとN-K個の赤いボールがあります。
    # すぬけ君と高橋君はこれらのボールで遊んでいます。
    # 高橋君は、1 回の操作で連続して並ぶ青いボールを何個でも回収することができます。
    # 高橋君は、常に K 個の青いボールを回収するのにかかる操作の回数が最小になるように行動します。

    # 高橋君は、常に K 個の青いボールを回収するのにかかる操作の回数が最小になるように行動します。
    # K個の青いボールを回収するために高橋君がちょうどi回操作をする必要があるボールの並べ方は何通りあるでしょうか。
    # 1 ≤ i ≤ K をみたす i それぞれについて答えを計算し、 10^9+7 で割った余りを答えてください。

    # N個のボールを左から右に一列に並べます。
    # これらのうち K 個の青いボールのみを回収します。

    # K個の青いボールを回収するために高橋君がちょうどi回操作をする必要があるボールの並べ方は何通りあるでしょうか。
    # N個のボールを左から右に一列に並べます。
    # これらのうち K 個の青

=======
Suggestion 4

def nCk(n, k):
    a = 1
    b = 1
    for i in range(k):
        a *= (n - i)
        b *= (i + 1)
    return a // b

=======
Suggestion 5

def main():
    mod = 10**9 + 7
    N, K = map(int, input().split())
    for i in range(1, K+1):
        print((comb(N-K+1, i, mod) * comb(K-1, i-1, mod)) % mod)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    MOD = 10 ** 9 + 7
    # dp[i][j]: 青いボールが i 個、赤いボールが j 個あるときの並べ方の総数
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N + 1):
        for j in range(N + 1):
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= MOD
    for i in range(1, K + 1):
        ans = dp[i][N - i] * dp[K - i][N - K]
        ans %= MOD
        print(ans)

=======
Suggestion 7

def main():
    #入力
    N,K=map(int,input().split())
    #K個の青いボールとN-K個の赤いボールがあります。同じ色のボールは区別が不可能です。
    #すぬけ君と高橋君はこれらのボールで遊んでいます。
    #まず、すぬけ君が、N 個のボールを左から右に一列に並べます。
    #次に、高橋君は、これらのうち K 個の青いボールのみを回収します。
    #高橋君は、1 回の操作で連続して並ぶ青いボールを何個でも回収することができます。
    #高橋君は、常に K 個の青いボールを回収するのにかかる操作の回数が最小になるように行動します。
    #K 個の青いボールを回収するために高橋君がちょうど i 回操作をする必要があるボールの並べ方は何通りあるでしょうか。
    #1 ≤ i ≤ K をみたす i それぞれについて答えを計算し、 10^9+7 で割った余りを答えてください。
    #制約
    #1 ≤ K ≤ N ≤ 2000
    #入力
    #入力は以下の形式で標準入力から与えられる。
    #N K
    #出力
    #i 行目 (1 ≤ i ≤ K) に高橋君がちょうど i 回操作をする必要があるボールの並べ方の総数を 10^9+7 で割った余りを

=======
Suggestion 8

def modinv(n, p):
    return pow(n, p - 2, p)
